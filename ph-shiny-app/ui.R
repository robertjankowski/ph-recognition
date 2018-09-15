library(shinythemes)

fluidPage(theme=shinytheme("journal"),

    titlePanel("ph-recognition"),
    
    sidebarLayout(
        sidebarPanel(
            fileInput("file1", "Choose image",
                      accept = c(
                          "image/png", "image/jpeg")
            ),

            tags$hr(),
            column(width = 12,
                   verbatimTextOutput("click_info")
            )
        ),
        mainPanel(
            imageOutput("image", click = "image_click")
        )
    )
)

