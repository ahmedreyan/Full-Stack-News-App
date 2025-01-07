/** @type {import('next').NextConfig} */
const nextConfig = {
  images: { 
    domains: ['newsapi.org'],
    unoptimized: true 
  },
  output: 'export'
};

module.exports = nextConfig;
