from Solution import Solution
from timeout_decorator import timeout
import unittest

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testcases = {
            "test_case_basic_two_step_jump": ([2,3,1,1,4], 2),
            "test_case_zero_in_the_path": ([2,3,0,1,4], 2),
            "test_case_single_element_already_at_end": ([0], 0),
            "test_case_all_maximum_jumps": ([6,4,3,2,1,0,0], 1),
            "test_case_slow_but_steady": ([1,1,1,1,1], 4),
            "test_case_large_jump_at_start": ([6,2,4,0,5,1,1,4,2,9], 2),
            "test_case_zeros_but_reachable": ([3,2,1,0,4,2,1], 3),
            "test_case_multiple_paths_choose_optimal": ([2,1,1,1,1], 3),
            "test_case_large_input_small_steps": ([1] * 10000, 9999),
            "test_case_optimal_early_jump": ([4,1,1,3,1,1,1], 2)
        }
        self.__solution = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_case_basic_two_step_jump(self):
        nums, output = self.__testcases['test_case_basic_two_step_jump']
        self.assertEqual(self.__solution.jump(nums), output)
    
    @timeout(0.5)
    def test_case_zero_in_the_path(self):
        nums, output = self.__testcases['test_case_zero_in_the_path']
        self.assertEqual(self.__solution.jump(nums), output)

    @timeout(0.5)
    def test_case_single_element_already_at_end(self):
        nums, output = self.__testcases['test_case_single_element_already_at_end']
        self.assertEqual(self.__solution.jump(nums), output)

    @timeout(0.5)
    def test_case_all_maximum_jumps(self):
        nums, output = self.__testcases['test_case_all_maximum_jumps']
        self.assertEqual(self.__solution.jump(nums), output)

    @timeout(0.5)
    def test_case_slow_but_steady(self):
        nums, output = self.__testcases['test_case_slow_but_steady']
        self.assertEqual(self.__solution.jump(nums), output)
    
    @timeout(0.5)
    def test_case_large_jump_at_start(self):
        nums, output = self.__testcases['test_case_large_jump_at_start']
        self.assertEqual(self.__solution.jump(nums), output)

    @timeout(0.5)
    def test_case_zeros_but_reachable(self):
        nums, output = self.__testcases['test_case_zeros_but_reachable']
        self.assertEqual(self.__solution.jump(nums), output)

    @timeout(0.5)
    def test_case_multiple_paths_choose_optimal(self):
        nums, output = self.__testcases['test_case_multiple_paths_choose_optimal']
        self.assertEqual(self.__solution.jump(nums), output)

    @timeout(0.5)
    def test_case_large_input_small_steps(self):
        nums, output = self.__testcases['test_case_large_input_small_steps']
        self.assertEqual(self.__solution.jump(nums), output)

    @timeout(0.5)
    def test_case_optimal_early_jump(self):
        nums, output = self.__testcases['test_case_optimal_early_jump']
        self.assertEqual(self.__solution.jump(nums), output)

if __name__ == '__main__': unittest.main()