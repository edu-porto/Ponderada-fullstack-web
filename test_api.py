#!/usr/bin/env python3
"""
Test script for the Product App backend API
"""

import requests
import json
import time

BASE_URL = "http://localhost:5000"

def test_api():
    print("Testing Product App Backend API...")
    print("=" * 50)
    
    # Test 1: Get products (should work without auth)
    print("1. Testing GET /api/products")
    try:
        response = requests.get(f"{BASE_URL}/api/products")
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Success: Found {len(data['products'])} products")
        else:
            print(f"   ❌ Failed: Status {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 2: Register a new user
    print("\n2. Testing POST /api/register")
    test_user = {
        "name": "Test User",
        "email": "test@example.com",
        "password": "test123"
    }
    try:
        response = requests.post(f"{BASE_URL}/api/register", json=test_user)
        if response.status_code == 201:
            print("   ✅ Success: User registered")
        elif response.status_code == 400:
            print("   ⚠️  User already exists (expected if running multiple times)")
        else:
            print(f"   ❌ Failed: Status {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 3: Login with the test user
    print("\n3. Testing POST /api/login")
    login_data = {
        "email": "test@example.com",
        "password": "test123"
    }
    token = None
    try:
        response = requests.post(f"{BASE_URL}/api/login", json=login_data)
        if response.status_code == 200:
            data = response.json()
            token = data['token']
            print(f"   ✅ Success: Logged in, token: {token[:20]}...")
        else:
            print(f"   ❌ Failed: Status {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 4: Create a product (requires auth)
    if token:
        print("\n4. Testing POST /api/products (with auth)")
        product_data = {
            "name": "Test Product",
            "description": "This is a test product created by the test script",
            "price": 29.99,
            "image_url": "https://picsum.photos/300/300?random=test"
        }
        try:
            headers = {"Authorization": f"Bearer {token}"}
            response = requests.post(f"{BASE_URL}/api/products", json=product_data, headers=headers)
            if response.status_code == 201:
                print("   ✅ Success: Product created")
            else:
                print(f"   ❌ Failed: Status {response.status_code}")
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    # Test 5: Get notifications
    print("\n5. Testing GET /api/notifications")
    try:
        response = requests.get(f"{BASE_URL}/api/notifications")
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Success: Found {len(data['notifications'])} notifications")
        else:
            print(f"   ❌ Failed: Status {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    print("\n" + "=" * 50)
    print("API testing completed!")

if __name__ == "__main__":
    # Wait a moment for server to be ready
    print("Waiting for server to be ready...")
    time.sleep(3)
    test_api()

