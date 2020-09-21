# net-shutdown
Issue a shutdown command over an HTTP network call


## Installation
```shell script
git clone https://github.com/Kyle-Falconer/net-shutdown.git && cd net-shutdown
pip install -r requirements.txt
```

## Running the server

```shell script
sudo python ShutdownServer.py
```

Alternatively, if you don't want to run python as root, then add user to use as the web service owner and add that user to the sudoers list. For more information on this, see https://stackoverflow.com/a/41215183/940217

Then, the next request made to [http://localhost:5000](http://localhost:5000) will trigger a shutdown
