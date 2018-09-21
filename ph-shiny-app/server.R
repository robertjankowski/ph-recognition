library(tools)

function(input, output, session) {

    terms <- reactive({
        if(!is.null(input$file1)) {
            file1 = input$file1   
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
        req(input$file1)
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
        req(input$file1)
        # TODO
        # store model in cache
        x <- input$image_click$x
        y <- input$image_click$y
        width  <- session$clientData$output_image_width
        height <- session$clientData$output_image_height
        tryCatch(
            {
                processImage(x, y, input$file1$datapath, width, height, input$model)
            }, error = function(cond) {
                # not show unnecessary error
                cat("Click on image to get PH")
            }
        )
        
    })
    
}