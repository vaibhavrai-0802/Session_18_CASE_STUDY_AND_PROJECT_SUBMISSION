{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def fib2(max_limit):\n",
    "    fib_list = [1,1]\n",
    "    for i in range(2, max_limit):\n",
    "        next_item = fib_list[i-1] + fib_list[i-2]\n",
    "        if next_item < max_limit:\n",
    "            fib_list.append(next_item)\n",
    "        else:\n",
    "            break\n",
    "    return fib_list"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
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
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
