import unittest
import sys

if __name__ == '__main__':
  print("\n================= RUNNING CAPOV TEST SUITE =================\n")
  loader = unittest.TestLoader()
  suite = loader.discover('capov/tests')
  runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=2)
  result = runner.run(suite)

  print("\n================= SUMMARY =================")
  print(f"Ran {result.testsRun} test(s)")
  if result.wasSuccessful():
    print("RESULT: ✅ All tests passed")
  else:
    print("RESULT: ❌ Some tests failed")
    print("Failures:", len(result.failures))
    print("Errors:", len(result.errors))