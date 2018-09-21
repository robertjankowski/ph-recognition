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
            ),
            tags$head(tags$style("#click_info
                                {
                                    font-size: 18px;
                                    font-style: bold;
                                }"
            )),
            tags$hr(),
            radioButtons("model", "Choose model:",
                         c("Binary classification" = "bin_clf",
                           "Mulitclass classification" = "multi_clf",
                           "Regression" = "reg_clf"))
        ),
        mainPanel(
            imageOutput("image", click = "image_click")
        )
    )
)

