library(jpeg)
library(OpenImageR)
library(imager)
library(tidyverse)
library(reshape2)

processImage <- function(mouse_x, mouse_y, files, width, height) {
    
    # TODO
    # 1. write .py script to load model and make prediction based on mouse position
    ## return predictions and display on the screen
    # 2. problem with RGB scale
    # 3. problem with resizing images !
    
    # file_type <- file_ext(files)
    # if (file_type == "jpg") {
    #     img <- readJPEG(files)
    #     
    # } else if (file_type == "png") {
    #     img <- readPNG(files)
    # } else {
    #     img <- readJPEG("images/ph_scale1.jpg")
    # }
    
    
    img <- load.image(files)
    # resize
    # img <- resize(img, width, height)
    
    df <- as.data.frame(img)
    df <- df %>% select(-cc)
    
    rgb_scale <- df %>% filter(x == floor(as.numeric(mouse_x))) %>%
                     filter(y == floor(as.numeric(mouse_y))) %>%
                     select(value) %>% mutate(value=value * 255.0)
    
    cat("X      = ", mouse_x)
    cat("\nY      = ", mouse_y)
    cat("\nwidth  = ", width)
    cat("\nheight = ", height, '\n')
    head(rgb_scale)
    
}
