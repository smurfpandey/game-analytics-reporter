from System.Net import WebRequest
from System.IO import StreamReader
from System.Text import Encoding
import clr

# clr.AddReferenceToFile("libs\\Newtonsoft.Json.dll")
clr.AddReference('System.Web.Extensions')
from System.Web.Script.Serialization import JavaScriptSerializer #since .net 3.5?

API_SERVER_URI = "http://requestbin.net/r/1ayyter1"


def PostData(jsonBody):
    request = WebRequest.Create(API_SERVER_URI)
    request.ContentType = "application/json"
    request.Method = "POST"
    bytes = Encoding.ASCII.GetBytes(jsonBody)
    request.ContentLength = bytes.Length
    reqStream = request.GetRequestStream()
    reqStream.Write(bytes, 0, bytes.Length)
    reqStream.Close()



def on_game_started(game):
    json=JavaScriptSerializer().Serialize(game)
    PostData(json)
    pass


def on_game_stopped(game, elapsed_seconds):
    pass
