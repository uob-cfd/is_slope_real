test = {
  'name': 'Question 3 ls ckd',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the values for 'best_c_ckd' and 'best_s_ckd'
          >>> 'best_c_ckd' in vars()
          True
          >>> 'best_c_ckd' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'best_c_ckd' and / or
          >>> # 'best_s_ckd' from their initial state (of ...)
          >>> best_c_ckd is not ...
          True
          >>> best_s_ckd is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose([15.3598, -0.98756], [best_c_ckd, best_s_ckd])
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
