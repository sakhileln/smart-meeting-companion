# Build stage
FROM debian:latest AS build-env

# Install flutter dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    unzip \
    xz-utils \
    zip \
    libglu1-mesa

# Clone the flutter repo
RUN git clone https://github.com/flutter/flutter.git /usr/local/flutter

# Set flutter path
ENV PATH="${PATH}:/usr/local/flutter/bin:/usr/local/flutter/bin/cache/dart-sdk/bin"

# Enable flutter web
RUN flutter doctor
RUN flutter config --enable-web

# Run flutter doctor
RUN flutter doctor -v

# Copy files to container and build
WORKDIR /app
COPY . .

# Get dependencies
RUN flutter pub get

# Build the app for the web
RUN flutter build web --release

# Production stage
FROM nginx:stable-alpine

# Copy built app and nginx config
COPY --from=build-env /app/build/web /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
