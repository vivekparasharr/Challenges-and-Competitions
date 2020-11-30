
# https://www.tylermw.com/a-step-by-step-guide-to-making-3d-maps-with-satellite-imagery-in-r/

# download elevation data
# elevation data is the Shuttle Radar Topography Mission (SRTM) dataset
# It’s a global 30 meter resolution dataset (meaning, 30m between each point)
# https://dwtkns.com/srtm30m/

# download satellite imagery data
# We specifically want Landsat 8 data
# https://earthexplorer.usgs.gov/

# install.packages(c("rayshader", "raster", "sp"))
library(rayshader)
library(sp)
library(raster)
library(scales)

# start with loading the elevation dataset
zion_elevation = raster::raster("2/N10E092.hgt")

height_shade(raster_to_matrix(zion_elevation)) %>%
  plot_map()
  
# let’s load our georeferenced satellite imagery. 
# The red, blue, and green bands on Landsat 8 data are bands B4, B3, and B2, respectively. 
# You can delete the rest of the bands
zion_r = raster::raster("2/LC08_L1TP_134053_20140309_20170425_01_T1_B4.TIF")
zion_g = raster::raster("2/LC08_L1TP_134053_20140309_20170425_01_T1_B3.TIF")
zion_b = raster::raster("2/LC08_L1TP_134053_20140309_20170425_01_T1_B2.TIF")

zion_rbg = raster::stack(zion_r, zion_g, zion_b)
raster::plotRGB(zion_rbg, scale=255^2)

# Why is it so dark? We need to apply a gamma correction to the the imagery, 
# which corrects raw linear intensity data for our non-linear perception of darkness. 
# We do that simply by taking the square root of the data (we can also remove the scale argument).
zion_rbg_corrected = sqrt(raster::stack(zion_r, zion_g, zion_b))
raster::plotRGB(zion_rbg_corrected)

# the coordinate reference systems of our elevation data and imagery data don’t match! Oh no.
raster::crs(zion_r)
raster::crs(zion_elevation)

# transform the elevation data from long/lat to UTM with the raster::projectRaster() function. 
# We use the “bilinear” method for interpolation since elevation is a continuous variable.
crs(zion_r)
zion_elevation_utm = raster::projectRaster(zion_elevation, crs = crs(zion_r), method = "bilinear")
crs(zion_elevation_utm)


# crop the region down to the park itself.
# To figure out what long/lat values enclosed our area, go to Google Maps and double click 
# on the map to extract the bottom left and top right corners of the bounding box for the final map
bottom_left = c(y=92.332766, x=10.500009)
top_right   = c(y=92.615658, x=10.906591)
# use the sp package to transform these long/lat coords into UTM coordinates
extent_latlong = sp::SpatialPoints(rbind(bottom_left, top_right), proj4string=sp::CRS("+proj=longlat +ellps=WGS84 +datum=WGS84"))
extent_utm = sp::spTransform(extent_latlong, raster::crs(zion_elevation_utm))

e = raster::extent(extent_utm)
e


# Now we’ll crop our datasets to the same region, and create an 3-layer RGB array of the image intensities. This is what rayshader needs as input to drape over the elevation values. We also need to transpose the array, since rasters and arrays are oriented differently in R, because of course they are🙄. We do that with the aperm() function, which performs a multi-dimensional transpose. We’ll also convert our elevation data to a base R matrix, which is what rayshader expects for elevation data.
zion_rgb_cropped = raster::crop(zion_rbg_corrected, e)
elevation_cropped = raster::crop(zion_elevation_utm, e)

names(zion_rgb_cropped) = c("r","g","b")

zion_r_cropped = rayshader::raster_to_matrix(zion_rgb_cropped$r)
zion_g_cropped = rayshader::raster_to_matrix(zion_rgb_cropped$g)
zion_b_cropped = rayshader::raster_to_matrix(zion_rgb_cropped$b)

zionel_matrix = rayshader::raster_to_matrix(elevation_cropped)

zion_rgb_array = array(0,dim=c(nrow(zion_r_cropped),ncol(zion_r_cropped),3))

zion_rgb_array[,,1] = zion_r_cropped/255 #Red layer
zion_rgb_array[,,2] = zion_g_cropped/255 #Blue layer
zion_rgb_array[,,3] = zion_b_cropped/255 #Green layer

zion_rgb_array = aperm(zion_rgb_array, c(2,1,3))

plot_map(zion_rgb_array)

# We will also now scale our data to improve the contrast and make the image more vibrant. I’m going to use the scales package to rescale the image to use the full range of color.
zion_rgb_contrast = scales::rescale(zion_rgb_array,to=c(0,1))

plot_map(zion_rgb_contrast)

# Now we just input this image into plot_3d() along with our elevation data.
# For a realistic landscape, we should set zscale = 30 (since the elevation data was taken at 30 meter increments), but we’re going to set zscale = 15 to give the landscape 2x exaggeration
plot_3d(zion_rgb_contrast, zionel_matrix, windowsize = c(1100,900), zscale = 15, shadowdepth = -50,
        zoom=0.5, phi=45,theta=-45,fov=70, background = "#F2E1D0", shadowcolor = "#523E2B")
render_snapshot(title_text = "Little Andaman Island | Imagery: Landsat 8 | DEM: 30m SRTM",
                title_bar_color = "#1f5214", title_color = "white", title_bar_alpha = 1)

# The static snapshot above is nice, but 3D is best seen in motion, so let’s create a movie of us rotating around the scene. We’ll move the camera with render_camera(), and generate 1440 frames with render_snapshot(). At 60 frames per second, this will generate a 24 second video. You can do this via the av package, but I’m going to call ffmpeg directly via a system() call, since the output of av doesn’t seem to play nicely with embeddable web videos (for some reason).
angles= seq(0,360,length.out = 1441)[-1]
for(i in 1:1440) {
  render_camera(theta=-45+angles[i])
  render_snapshot(filename = sprintf("zionpark%i.png", i), 
                  title_text = "Zion National Park, Utah | Imagery: Landsat 8 | DEM: 30m SRTM",
                  title_bar_color = "#1f5214", title_color = "white", title_bar_alpha = 1)
}
rgl::rgl.close()

#av::av_encode_video(sprintf("zionpark%d.png",seq(1,1440,by=1)), framerate = 30,
# output = "zionpark.mp4")

rgl::rgl.close()
system("ffmpeg -framerate 60 -i zionpark%d.png -pix_fmt yuv420p zionpark.mp4")



