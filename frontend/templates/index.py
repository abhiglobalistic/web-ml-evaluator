# Home page layout for the application
import dash_html_components as html
import dash_core_components as dcc

class index:

    def getTabs(self):
        return dcc.Tabs(id='main-tabs', value='tab-1', children=[
                dcc.Tab(label='Dataset Explorer', value='tab-1'),
                dcc.Tab(label='Algorithm Selector', value='tab-2'),
                dcc.Tab(label='Evaluate', value='tab-3'),
                dcc.Tab(label='Results', value='tab-4'),
            ])

    def createIndexLayout(self):

        tabs = self.getTabs()
        header = html.H4('Machine learning Evaluator',style={'text-align':'center'})
        layout =  html.Div([
            header,
            tabs
        ],className='container')

        return layout
