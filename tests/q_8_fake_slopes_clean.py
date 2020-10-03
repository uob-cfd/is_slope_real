test = {
  'name': 'Question 3 ls ckd',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(fake_slopes_clean)
          1000
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Mean should be near 0.
          >>> -0.039 < np.mean(fake_slopes_clean) < 0.039
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # std should be between 0.35 and 0.42
          >>> 0.35 < np.std(fake_slopes_clean) < 0.42
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
# Use algebraic least-squares solution.
X = np.ones((len(hgb_clean), 2)) X[:, 1] = hgb_clean   # Design matrix.
pX = np.linalg.pinv(X)
n_iters = 1000000
fake_slopes_clean = np.zeros(n_iters)
for i in range(n_iters):
    np.random.shuffle(shuffled_creat_clean)
    fake_slopes_clean[i] = (pX @ shuffled_creat_clean)[1]
trials = np.reshape(fake_slopes_clean, (-1, 1000))
means = np.mean(trials, axis=1)
print(min(means), max(means))
stds = np.std(trials, axis=1)
print(min(stds), max(stds))
"""

"""
# Results, run1:
-0.038268416645194356 0.03776311302928808
0.3585775143676405 0.4089737871472806
# Results, run2:
-0.03694884909387602 0.03870940908700521
0.3558966006838831 0.418627611869601
"""
