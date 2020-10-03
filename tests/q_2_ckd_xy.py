test = {
  'name': 'Question 2 ckd xy',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the values for 'hgb_ckd' and 'creat_ckd'
          >>> 'hgb_ckd' in vars()
          True
          >>> 'hgb_ckd' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'hgb_ckd' and / or
          >>> # 'creat_ckd' from their initial state (of ...)
          >>> hgb_ckd is not ...
          True
          >>> creat_ckd is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(hgb_ckd)
          43
          >>> len(creat_ckd)
          43
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(hgb_ckd, np.ndarray)
          True
          >>> isinstance(creat_ckd, np.ndarray)
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
