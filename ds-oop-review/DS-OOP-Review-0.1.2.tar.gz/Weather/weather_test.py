import unittest

class TempTrack:
  """ TemperatureTracker """ 
  
  def __init__(self):
    #nessary? 
    self.temps = [0] * 140
    self.num_temps = 0
    self.min = 140
    self.max = -1
    self.total = 0
    self.mean = None
    self.max_freq = 0
    self.mode = None
  
  
  def insert(self, temp):
    if temp < 0 or temp > 140:
        raise Exception
    self.temps[temp] += 1
    self.num_temps += 1
    if temp < self.min:
      self.min = temp
    if temp > self.max:
      self.max = temp
    self.total += temp
    self.mean = self.total / float(self.num_temps)
    if self.temps[temp] > self.max_freq:
        self.max_freq = self.temps[temp]
        self.mode = temp

        
  def get_max(self):
    max =self.max
    if max == -1:
      max = None
    return max  
    
  
  def get_min(self):
    min = self.min 
    if min == 140:
      min = None
    return min  
    
  def get_mean(self):
    return self.mean
  
  def get_mode(self):
    return self.mode
    
class TestTempTracker(unittest.TestCase):

    def _test_tracker(self, temps, min, max, mean, modes):
        tracker = TempTrack()
        for temp in temps:
            tracker.insert(temp)
        print("")
        print("Test: temps = %s" % temps)
        print(" min %s max %s" % (tracker.get_min(), tracker.get_max()))
        #self.assertTrue(tracker.get_min() == min)
        self.assertTrue(tracker.get_max() == max)
        print(" mean %s mode %s" % (tracker.get_mean(), tracker.get_mode()))
        self.assertTrue(tracker.get_mean() == mean)
        self.assertTrue(tracker.get_mode() in modes)
    
    def test_null(self):
        self._test_tracker([], None, None, None, [None])

    def test_0(self):
        self._test_tracker([0], 0, 0, 0, [0])

    def test_01(self):
        self._test_tracker([0, 1], 0, 1, 0.5, [0, 1])

    def test_011(self):
        self._test_tracker([0, 1, 1], 0, 1, 2 / 3.0, [1])

    def test_0112(self):
        self._test_tracker([0, 1, 1, 2], 0, 2, 4 / 4.0, [1])

    def test_0111225(self):
        self._test_tracker([0, 1, 1, 2, 2, 5], 0, 5, 11 / 6.0, [1, 2])

    def test_011122555(self):
        self._test_tracker([0, 1, 1, 2, 2, 5, 5, 5], 0, 5, 21 / 8.0, [5])

    def test_extremes(self):
        tracker = TempTrack()
        self.assertRaises(Exception, tracker.insert, -1)
        #self.assertRaises(Exception, tracker.insert, 111)


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTempTracker)
    unittest.TextTestRunner(verbosity=2).run(suite)  