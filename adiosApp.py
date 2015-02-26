#!/usr/bin/python
import webapp;

class adiosApp(webapp.webApp):

    def process(self,parsedRequest):
        """Parse"""
        return ("200 OK","<html><body><b>Adios mundo cruel!</h1></body></html>")

if __name__ == "__main__":
    testWebApp = adiosApp("localhost",1234);

