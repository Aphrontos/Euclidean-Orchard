# Coprimes

## Description
This is a visulization of Dirichlet's Theorem on Arithmetic Progressions.

The theorem states that a linear expression an + b contains infinite primes if a and b are coprime.

Each pixel is black if the x-coordinate and y-coordinate are coprime, white if not. This is equivalent to the theorem.

Proof: 

(an + b) mod a = b mod a

x ≔ an

y ≔ b

(x + y) mod x = y mod x

## Usage
This program generates a PNG based on Dirichlet's Theorem on Arithmetic Progression.

The code uses Python's zlib, and is ridiculously slow. Use if you have the patience.

A PNG named "Pattern.png" will be generated in the same directory where you put the Python code.

You can specify the dimensions, height then width.

Note: a 1920 by 1080 PNG takes ~10-15 minutes to generate on my laptop. You've been warned for the 2nd time.

## Motivation
I just felt curious what will happen and how it would look like. 

I'm also a fan of odd wallpapers, especially if they're generated using a mathematical concepts.
