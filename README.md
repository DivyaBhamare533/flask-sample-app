# Flask Sample App

## Overview

This is a simple Flask web application developed using Python.

## Features

- Built using Flask
- No HTML files
- Returns JSON responses
- REST API endpoints

## Endpoints

### Home

GET /

Returns:

```json
{
  "message": "Welcome to Flask!",
  "status": "success"
}
```

### About

GET /about

### Health

GET /health

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

The application runs on:

http://127.0.0.1:5000