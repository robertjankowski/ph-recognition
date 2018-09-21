library(jpeg)
library(OpenImageR)
library(imager)
library(tidyverse)
library(reshape2)

processImage <- function(mouse_x, mouse_y, files, width, height, model) {
    
    img <- load.image(files)
    
    # resize
    # TODO
    # 3. problem with resizing images !
    # img <- resize(img, width, height)
    
    df <- as.data.frame(img)
    df <- df %>% select(-cc)
    
    rgb_scale <- df %>% filter(x == floor(as.numeric(mouse_x))) %>%
                     filter(y == floor(as.numeric(mouse_y))) %>%
                     select(value) %>% mutate(value=value * 255.0)
    
    red <- rgb_scale$value[1]
    green <- rgb_scale$value[2]
    blue <- rgb_scale$value[3]
    
    result <- system(paste("python predict.py", red, green, blue, model), intern = TRUE)
    
    cat("X      = ", mouse_x)
    cat("\nY      = ", mouse_y)
    cat("\nwidth  = ", width)
    cat("\nheight = ", height, '\n')
    
    cat(result)
}
