library(tools)

function(input, output, session) {

    terms <- reactive({

        file1 = input$file1
        if (is.null(file1)) {
            return(NULL)
        }
        input$update
        isolate({
            withProgress({
                setProgress(message = "Processing corpus...")
            })
        })
    })
    
    output$image <- renderImage({
        width  <- session$clientData$output_image_width
        height <- session$clientData$output_image_height
        
        # test image
        if (is.null(input$file1)) {
            return(list(
                src = "images/ph_scale1.jpg",
                contentType = "image/jpeg", # "image/png"
                width = width,
                height = height,
                alt = "image"
            ))
        }
        
        # render input file
        img <- input$file1$datapath
        type <- file_ext(img)
        return(list(
            src = input$file1$datapath,
            contentType = ifelse(type == "png", "image/png", "image/jpeg"),
            # width = width, # only for tests
            # height = height,
            alt = "image"
        ))
        
    }, deleteFile = FALSE)
    
    output$click_info <- renderPrint({
        x <- input$image_click$x
        y <- input$image_click$y
        width  <- session$clientData$output_image_width
        height <- session$clientData$output_image_height
        if(!is.null(input$file1)) {
            processImage(x, y, input$file1$datapath, width, height)   
        }
    })
    
}