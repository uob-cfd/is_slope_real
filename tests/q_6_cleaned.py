test = {
  'name': 'Question 6_cleaned',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'hgb_clean'
          >>> 'hgb_clean' in vars()
          True
          >>> # You need to set the value for 'creat_clean'
          >>> 'creat_clean' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'hgb_clean'
          >>> # from its initial state (of ...)
          >>> hgb_clean is not ...
          True
          >>> # You haven't changed the value for 'creat_clean'
          >>> # from its initial state (of ...)
          >>> creat_clean is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(hgb_clean, np.ndarray)
          True
          >>> isinstance(creat_clean, np.ndarray)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(hgb_clean)
          41
          >>> len(creat_clean)
          41
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.sum(hgb_clean)
          400.9
          >>> np.sum(creat_clean)
          230.6
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
