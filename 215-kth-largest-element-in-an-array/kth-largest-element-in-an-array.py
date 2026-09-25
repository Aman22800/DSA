class Solution:
    def findKthLargest(self, nums, k):

        # Convert kth largest into an index
        # Example: n = 6, k = 2
        # target = 6 - 2 = 4
        # So we need the element at index 4
        target = len(nums) - k

        def quickselect(left, right):

            # Choose a pivot from the middle
            pivot = nums[(left + right) // 2]

            # Three regions:
            # [left ... lt-1]  -> elements smaller than pivot
            # [lt ... gt]      -> elements equal to pivot
            # [gt+1 ... right]  -> elements greater than pivot

            lt = left
            i = left
            gt = right

            # Process elements until i crosses gt
            while i <= gt:

                # Case 1: current element is smaller than pivot
                if nums[i] < pivot:

                    # Move it to the left section
                    nums[lt], nums[i] = nums[i], nums[lt]

                    lt += 1
                    i += 1

                # Case 2: current element is greater than pivot
                elif nums[i] > pivot:

                    # Move it to the right section
                    nums[i], nums[gt] = nums[gt], nums[i]

                    gt -= 1

                    # Don't increment i here.
                    # The element swapped from gt still needs checking.

                # Case 3: current element equals pivot
                else:

                    # It already belongs in the middle section
                    i += 1

            # Now the array is divided into:
            #
            # [ smaller | equal | greater ]
            #
            #             lt    gt

            # Target is in the smaller section
            if target < lt:
                return quickselect(left, lt - 1)

            # Target is in the greater section
            elif target > gt:
                return quickselect(gt + 1, right)

            # Target is inside the equal section
            else:
                return pivot

        return quickselect(0, len(nums) - 1)