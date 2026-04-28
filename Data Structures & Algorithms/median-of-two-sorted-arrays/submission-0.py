class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        n1, n2 = len(nums1), len(nums2)
        total = n1 + n2
        half = (total + 1) // 2  # elements on the left side of the partition

        left, right = 0, n1
        while left <= right:
            cut1 = (left + right) // 2
            cut2 = half - cut1

            # Borders of partitions
            l1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            r1 = float('inf') if cut1 == n1 else nums1[cut1]

            l2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
            r2 = float('inf') if cut2 == n2 else nums2[cut2]

            # Check if correct partition
            if l1 <= r2 and l2 <= r1:
                if total % 2 == 1:
                    return float(max(l1, l2))
                return (max(l1, l2) + min(r1, r2)) / 2.0

            # Move search space
            if l1 > r2:
                right = cut1 - 1
            else:
                left = cut1 + 1

        # Should never reach here if inputs are valid
        return 0.0