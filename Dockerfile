# Use the official Python image from the Docker Hub
FROM python:3.12.6-slim

# Set the working directory
WORKDIR /app

# Install necessary system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gnupg \
        git \
        wget \
        curl \
        unzip \
        xvfb \
        libxi6 \
        libgconf-2-4 \
        default-jdk \
        fonts-liberation \
        libappindicator3-1 \
        libatk-bridge2.0-0 \
        libatk1.0-0 \
        libcups2 \
        libdbus-1-3 \
        libgdk-pixbuf2.0-0 \
        libglib2.0-0 \
        libnss3 \
        libx11-xcb1 \
        libxcomposite1 \
        libxrandr2 \
        libxss1 \
        libxtst6 \
        xdg-utils \
        && rm -rf /var/lib/apt/lists/*

# Install Google Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable

# Install ChromeDriver
RUN CHROME_DRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
    wget -N https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    rm chromedriver_linux64.zip && \
    mv chromedriver /usr/local/bin/chromedriver && \
    chmod +x /usr/local/bin/chromedriver

# Add ChromeDriver to PATH
ENV PATH="/usr/local/bin/chromedriver:${PATH}"

# Clone the GitHub repository
RUN git clone https://github.com/ShreyuKiBhuvi/SamplePythonSeleniumAutomationFramework.git /temp_dir && \
    cp -r /temp_dir/* . && \
    rm -rf /temp_dir

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run your tests
CMD ["xvfb-run", "-a", "pytest", "--html=report.html", "--alluredir=allure-results"]
