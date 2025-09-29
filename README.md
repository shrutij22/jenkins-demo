# Jenkins Java Pipeline with Artifact Management

This repository showcases a streamlined Jenkins pipeline that takes your Java code from source to artifact with ease. It:

- **Compiles** your Java program automatically  
- **Runs** the program to verify it works  
- **Archives** the generated JAR file as a build artifact for easy access  
- Provides a handy Python script that effortlessly fetches the latest successful JAR from Jenkins — so you always have the freshest build on hand!

With this setup, continuous integration and artifact management become smooth and hassle-free.

---

## Quick: Serve a `.jar` from this machine (for local network)

If you want to quickly share the JAR file on your local network, follow these steps:

1. Place `downloaded.jar` in the folder you want to serve (e.g. `/root` or `~/myfiles`).

2. Start a simple HTTP server by running:

    ```bash
    cd /root          # or the directory containing downloaded.jar
    python3 -m http.server 8000 --bind 0.0.0.0
    ```

3. Open a browser on another machine in the same network and go to:

    ```
    http://<IP>:8000/downloaded.jar
    ```

    Replace `<IP>` with the IP address of the machine running the server (e.g., `192.168.1.10`).

> ⚠️ **Security Note:** This method serves files without authentication and is intended for trusted local networks only. Do not expose this to the public internet. Stop the server by pressing `Ctrl+C` when done.

---

## Additional Recommendations

- For production or broader distribution, consider uploading your `.jar` to GitHub Releases or an artifact repository.
- Automate artifact publishing using Jenkins post-build steps or GitHub Actions for seamless delivery.
- Always ensure your network and firewall settings permit the traffic for the HTTP server port (default 8000).

---

Feel free to reach out or contribute to improve this pipeline!

