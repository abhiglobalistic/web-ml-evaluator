# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import frontend.templates.index as mainLayout

class setup:

    def __init__(self,title,debug):

        self.title = title
        self.debug = debug

        # default css setup and app title
        self.external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css']
        self.app = dash.Dash(__name__, external_stylesheets=self.external_stylesheets)
        self.app.title = self.title

        indexPage = mainLayout.index()
        self.app.layout = indexPage.createIndexLayout()


    def getApplication(self):
        """
        :return:
        :rtype:
        """
        # get the base app
        return self.app

    def runApplication(self,debug):
        """
        :param debug:
        :type debug:
        """
        # run the application
        # with debug args provided
        # default debug is True
        if self.debug is None:
            self.debug = True

        self.app.run_server(debug=self.debug)










