#!/usr/bin/python
import webapp;

class holaApp(webapp.webApp):

    def process(self,parsedRequest):
        """Parse"""
        return ("200 OK","<html><body><b>Hola Mundo!</h1></body></html>")

if __name__ == "__main__":
    testWebApp = holaApp("localhost",1234);
