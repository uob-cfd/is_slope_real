test = {
  'name': 'Question 4 fake slopes',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(fake_slopes)
          1000
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Mean should be near 0.
          >>> -0.036 < np.mean(fake_slopes) < 0.036
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # std should be between 0.27 and 0.33
          >>> 0.27 < np.std(fake_slopes) < 0.33
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

"""
# Estimating variation of stds.
X = np.ones((len(hgb_ckd), 2))
X[:, 1] = hgb_ckd   # Design matrix.
pX = np.linalg.pinv(X)
n_iters = 1000000
fake_slopes = np.zeros(n_iters)
for i in range(n_iters):
    np.random.shuffle(shuffled_creat)
    fake_slopes[i] = (pX @ shuffled_creat)[1]
trials = np.reshape(fake_slopes, (-1, 1000))
means = np.mean(trials, axis=1)
print(min(means), max(means))
stds = np.std(trials, axis=1)
print(min(stds), max(stds))
"""

"""
# Results, run1:
-0.02515461100783057 0.03417154902071242
0.278512820463332 0.32553396292327885
# Results, run2:
-0.03181787293673598 0.030050140367678765
0.2777941774983888 0.31852219513267355
"""
