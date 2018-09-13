library(shinythemes)

fluidPage(theme=shinytheme("journal"),

    titlePanel("ph-recognition"),
    
    sidebarLayout(
        sidebarPanel(
            fileInput("file1", "Choose image",
                      accept = c(
                          "image/png", "image/jpeg")
            ),

            tags$hr()
        ),
        mainPanel(
            imageOutput("image")
        )
    )
)

