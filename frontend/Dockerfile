# Use an Nginx image to serve the HTML
FROM nginx:alpine

# Copy the HTML file to the Nginx container
COPY index.html /usr/share/nginx/html/index.html

# Copy the Nginx configuration file
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
