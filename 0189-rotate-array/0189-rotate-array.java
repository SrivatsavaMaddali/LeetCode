class Solution {
    public void rotate(int[] nums, int k) {
        int length = nums.length;
        int rotations = k % length;

        reverse(nums, 0, length - 1); // Reverse the entire array
        reverse(nums, 0, rotations - 1); // Reverse the first 'rotations' elements
        reverse(nums, rotations, length - 1); // Reverse the remaining elements
    }

    private void reverse(int[] nums, int start, int end) {
        while (start < end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }
}
