test = {
  'name': 'Question 5_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like measurement_dates isn't an array.
          >>> import numpy as np
          >>> type(measurement_dates) == np.ndarray
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It looks like you're incrementing measurement dates by 1, but
          >>> # they happened every quarter, so they should go up by .25.
          >>> # The third argument to np.arange controls this.
          >>> not(all(np.diff(measurement_dates) == 1))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Each quarter should be .25 bigger than the previous one.
          >>> all(np.diff(measurement_dates) == 1/4)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # There appears to be an issue with the amount of values you have.
          >>> len(measurement_dates)
          106
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum(measurement_dates)
          212755.25
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
