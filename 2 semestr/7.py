def maximumSubarraySum(numbers):
  max_sum = -10**100  # Initialize with negative infinity

  for i in range(len(numbers)):
    current_sum = 0
    for j in range(i, len(numbers)):
      current_sum += numbers[j]
      if max_sum < current_sum:
        max_sum = current_sum


  print("Largest sum is ", max_sum)


numbers=list(int(input()) for i in range(int(input())))
maximumSubarraySum(numbers)