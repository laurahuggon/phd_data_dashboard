import dash # The main library for creating the Dash app
from dash import dcc, html  # dcc; Dash Core Components, used for interactive components like graphs and dropdowns
                            # html; a module within Dash that contains HTML components
from dash.dependencies import Input, Output # Used for creating callbacks to update the app's components
import dash_bootstrap_components as dbc # Used for styling the app with Bootstrap

# Initialise the app
# dash.Dash(__name__) creates the Dash app instance
# external_stylesheets=[dbc.themes.BOOTSTRAP] applies Bootstrap styling to the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create a list of dictionaries that represent the options for the dropdown menu
# Each dictionary has a 'label' (what the user sees) and a 'value' (the corresponding value for the option)
protein_options = [
    {'label': 'Synaptophysin', 'value': 'syp'},
    {'label': 'Syntaxin 1A', 'value': 'stx'},
    {'label': 'UNC13A', 'value': 'unc'},
    {'label': 'PSD-95', 'value': 'psd'},
    {'label': 'Homer', 'value': 'hmr'}
]

# Function to generate layout for selected protein
def generate_protein_layout(protein):   # This function takes a `protein` argument and returns a layout (HTML structure) specific to that protein
    return html.Div([  # A container for HTML elements
        # Row 1
        dbc.Row([
            dbc.Col([
                html.H3("Immunocytochemistry i3Neuron", className="text-center"),  # The main header
                html.P("DIV 21 | 18,500 CELLS/CM2",
                       className="text-center mt-2")  # Additional descriptive text beneath the header
            ], width=12)
        ]),

        # Row 2
        dbc.Row([
            dbc.Col([   # Column 1
                html.Div([  # A container for each image and its label
                    html.H4("Images", className="text-center"),  # A heading above the image
                    html.Img(src=f'/assets/{protein}/icc_wt.png', style={'width': '100%', 'display': 'block'})
                ], className="mb-4"),  # Adds margin to the bottom of images in the same column

                html.Div([
                    html.Img(src=f'/assets/{protein}/icc_qk.png', style={'width': '100%', 'display': 'block'})
                ], className="mb-4")
            ], style={'flex': '0 0 34%', 'max-width': '34%'}),

            dbc.Col([  # Column 2
                html.Div([  # A container for each image and its label
                    html.H4("Puncta Morphology", className="text-center"),
                    html.Img(src=f'/assets/{protein}/puncta_morphology.png', style={'width': '100%', 'display': 'block'})
                ]),
            ], style={'flex': '0 0 29.1%', 'max-width': '29.1%'}),

            dbc.Col([  # Column 3
                html.Div([
                    html.H4("Intensity", className="text-center"),
                    # Subcolumns within column 3
                    dbc.Row([
                        dbc.Col([   # Column 3.1
                            html.Div([
                                html.Img(src=f'/assets/{protein}/global_meanintensity.png',
                                         style={'width': '100%', 'display': 'block'})
                            ]),

                            html.Div([
                                html.Img(src=f'/assets/{protein}/global_medianintensity.png',
                                         style={'width': '100%', 'display': 'block'})
                            ]),

                            html.Div([
                                html.Img(src=f'/assets/{protein}/global_sumintensity.png',
                                         style={'width': '100%', 'display': 'block'})
                            ])
                        ], style={'flex': '0 0 33.33%', 'max-width': '33.33%'}),

                        dbc.Col([   # Column 3.2
                            html.Div([
                                html.Img(src=f'/assets/{protein}/cellbody_meanintensity.png',
                                         style={'width': '100%', 'display': 'block'})
                            ]),

                            html.Div([
                                html.Img(src=f'/assets/{protein}/cellbody_medianintensity.png',
                                         style={'width': '100%', 'display': 'block'})
                            ]),

                            html.Div([
                                html.Img(src=f'/assets/{protein}/cellbody_sumintensity.png',
                                         style={'width': '100%', 'display': 'block'})
                            ])
                        ], style={'flex': '0 0 33.33%', 'max-width': '33.33%'}),

                        dbc.Col([   # Column 3.3
                            html.Div([
                                html.Img(src=f'/assets/{protein}/puncta_meanintensity.png',
                                         style={'width': '100%', 'display': 'block'})
                            ]),

                            html.Div([
                                html.Img(src=f'/assets/{protein}/puncta_medianintensity.png',
                                         style={'width': '100%', 'display': 'block'})
                            ]),

                            html.Div([
                                html.Img(src=f'/assets/{protein}/puncta_sumintensity.png',
                                         style={'width': '100%', 'display': 'block'})
                            ])
                        ], style={'flex': '0 0 33.33%', 'max-width': '33.33%'})
                    ])
                ], style={'flex': '0 0 100%', 'max-width': '100%'}),
            ]),
        ]),

        # Row 3
        dbc.Row([
            dbc.Col([   # Column 1
                html.H3("Immunoblotting i3Neuron", className="text-center"),  # The main header
                html.P("DIV 21 | 73,000 CELLS/CM2",
                       className="text-center mt-2"),  # Additional descriptive text beneath the header
                # Subcolumns within column 1
                dbc.Row([
                    dbc.Col([   # Column 1.1
                        html.Div([  # A container for each image and its label
                            html.H4("Whole-Cell Lysate", className="text-center"),
                            html.Img(src=f'/assets/{protein}/i3neuron_wb.png', style={'width': '100%', 'display': 'block'})
                        ], className="mb-4")
                    ], width=6),

                    dbc.Col([   # Column 1.2
                        html.Div([  # A container for each image and its label
                            html.H4("Synaptosome", className="text-center")
                        ])
                    ], width=6)
                ])
            ], width=8),

            dbc.Col([  # Column 2
                html.H3("Immunoblotting Tg Mouse", className="text-center"),  # The main header
                html.P("12 MO | WHOLE BRAIN TISSUE",
                       className="text-center mt-2"),  # Additional descriptive text beneath the header

                html.Div([  # A container for each image and its label
                    html.H4("Synaptosome", className="text-center"),
                    html.Img(src=f'/assets/{protein}/mouse_wb.png', style={'width': '100%', 'display': 'block'})
                ], className="mb-4")
            ], width=4)
        ])
    ])

# Layout of the app
app.layout = dbc.Container([    # A container component from Bootstrap for layout
    dbc.Row([   # A row component for organising columns
        dbc.Col([   # A column component to place content within the row
            html.H1('Synaptic Proteins Dashboard'),  # A header for the dashboard
            dcc.Dropdown(   # A dropdown component for selecting proteins
                id='protein-dropdown',  # The ID used to reference this component in callbacks
                options=protein_options,    # The options for the dropdown menu
                value='syp',  # The default value of the dropdown
                clearable=False, # Prevents clearing the selection
                className='mb-4'  # Adds a bottom margin of size 4 (1.5rem)
            )
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col(id='protein-content', width=12) # A column to display the content that will be dynamically updated based on the dropdown selection
    ])
], fluid=True)

# Callback to update content based on dropdown selection
@app.callback(  # A decorator that defines the input and output of a callback function
    Output('protein-content', 'children'),  # Specifies that the output will update the `children` property of the component with ID `protein-content`
    [Input('protein-dropdown', 'value')]    # The callback is triggered whenever the value of the component with ID `protein-dropdown` changes
)
def update_content(protein):    # The function that generates and returns the new content based on the selected protein
    return generate_protein_layout(protein)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
