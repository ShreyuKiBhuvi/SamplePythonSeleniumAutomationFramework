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
RUN wget -q -O chrome.zip https://storage.googleapis.com/chrome-for-testing-public/129.0.6668.70/linux64/chrome-linux64.zip && \
    unzip chrome.zip -d /opt/ && \
    rm chrome.zip && \
    mv /opt/chrome-linux64 /opt/google-chrome && \
    ln -s /opt/google-chrome/chrome /usr/bin/google-chrome

# Install ChromeDriver
RUN wget -q -O chromedriver.zip https://storage.googleapis.com/chrome-for-testing-public/129.0.6668.70/linux64/chromedriver-linux64.zip && \
    unzip chromedriver.zip -d /opt/ && \
    rm chromedriver.zip && \
    mv /opt/chromedriver /usr/local/bin/chromedriver && \
    chmod +x /usr/local/bin/chromedriver

# Add ChromeDriver to PATH
ENV PATH="/usr/local/bin/chromedriver:${PATH}"

# Check Chrome and ChromeDriver versions
RUN google-chrome --version && chromedriver --version

# Set DISPLAY environment variable
ENV DISPLAY=:99

# Clone the GitHub repository
RUN git clone https://github.com/ShreyuKiBhuvi/SamplePythonSeleniumAutomationFramework.git /temp_dir && \
    cp -r /temp_dir/* . && \
    rm -rf /temp_dir

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run your tests
CMD ["xvfb-run", "-a", "pytest", "--html=report.html", "--alluredir=allure-results"]
