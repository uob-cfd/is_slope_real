test = {
  'name': 'Question 3 ls ckd',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the values for 'best_c_clean' and 'best_s_clean'
          >>> 'best_c_clean' in vars()
          True
          >>> 'best_c_clean' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'best_c_clean' and / or
          >>> # 'best_s_clean' from their initial state (of ...)
          >>> best_c_clean is not ...
          True
          >>> best_s_clean is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose([15.92391, -1.053331], [best_c_clean, best_s_clean])
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
