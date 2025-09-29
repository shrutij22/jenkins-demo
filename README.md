This repo showcases a streamlined Jenkins pipeline that takes your Java code from source to artifact with ease. It:

Compiles your Java program automatically,
Runs the program to verify it works,
Archives the generated JAR file as a build artifact for easy access,
And comes with a handy Python script that effortlessly fetches the latest successful JAR from Jenkins — so you always have the freshest build on hand!
With this setup, continuous integration and artifact management become smooth and hassle-free.

## Quick: serve a `.jar` from this machine (for local network)

1. Put `downloaded.jar` in the folder you want to serve (e.g. `/root` or `~/myfiles`).
2. Start a simple HTTP server:

```bash
cd /root            #  or the directory containing downloaded.jar
python3 -m http.server 8000 --bind 0.0.0.0
Open a browser and go to:
http://<IP>:8000/downloaded.jar
