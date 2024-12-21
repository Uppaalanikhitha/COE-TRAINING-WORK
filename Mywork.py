{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "18e254fe-bfa7-46eb-a0cb-1597b73e247c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "this is the user defined function\n",
      "without parameters and with return value\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'Hello'"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def add():\n",
    "    print(\"this is the user defined function\")\n",
    "    print(\"without parameters and with return value\")\n",
    "    return \"Hello\"\n",
    "add()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "1ccd14f8-e703-4bb2-adc2-f582cf32d492",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a password Nikkiuppala@1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "password is vaild\n"
     ]
    }
   ],
   "source": [
    "def check_pass_strength(password):\n",
    "    has_uppercase = False\n",
    "    has_lowercase = False\n",
    "    has_digit = False\n",
    "    has_special = False\n",
    "    special_characters = \"!@#$%^&*()-_=+[]{}|;:'\\\",.<>?/\"\n",
    "    if len(password)<10 or len(password)>15:\n",
    "        return \"password should contain at least 10 characters and max of 15 characters\"\n",
    "    if ' ' in password:\n",
    "        return \"weak password cannot accessed\"\n",
    "    if password.endswith('.') or password.endswith('@'):\n",
    "        return \"weak password cannot accessed\"\n",
    "    for char in password:\n",
    "        if char.isupper():\n",
    "            has_uppercase=True\n",
    "        elif char.islower():\n",
    "            has_lowercase=True\n",
    "        elif char.isdigit():\n",
    "            has_digit=True\n",
    "        elif char in special_characters:\n",
    "            has_special = True\n",
    "    if has_uppercase and has_lowercase and has_digit and has_special:\n",
    "        return \"password is vaild\"\n",
    "    else:\n",
    "        return \"password should have atleast one uppercase,lowercase letters ,digits and special character\"\n",
    "password=(input(\"Enter a password\"))\n",
    "result = check_pass_strength(password)\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "4d8a9cfc-dcf3-40b9-974d-0bec39e7a2aa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "700\n"
     ]
    }
   ],
   "source": [
    "a=[66,89,700,67,44,]\n",
    "b=[56,89,67]\n",
    "a.extend(b)\n",
    "print(a[7])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "73153466-8b3d-4481-ad57-67d1a058ec4b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Cart items:{'Laptop': 50000, 'Headphones': 2000, 'Mouse': 3500, 'Keyboard': 1500, 'Monitor': 8000, 'Usb Driver': 1000}\n",
      "Total price:59400.0\n"
     ]
    }
   ],
   "source": [
    "def calculate_total(cart):\n",
    "    total=sum(cart.values())\n",
    "    if total in range(20000,500000):\n",
    "        total*=0.9\n",
    "        return total\n",
    "    elif total>50000:\n",
    "        total=0.85\n",
    "        return total\n",
    "cart={'Laptop':50000,'Headphones':2000,'Mouse':3500,'Keyboard':1500,'Monitor':8000,'Usb Driver':1000}\n",
    "print(f\"Cart items:{cart}\")\n",
    "print(f\"Total price:{calculate_total(cart)}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2c1af8c7-46f3-42ab-a3e2-54ecccdb6715",
   "metadata": {},
   "outputs": [],
   "source": [
    "def add item(grocery"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cc8cc5f3-8e72-40a9-bbb0-5f4bb5f97f7a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "16e51f65-7f09-4f7f-8a7b-a28cbe91d437",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
