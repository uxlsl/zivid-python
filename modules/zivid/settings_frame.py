import _zivid


class Frame:
    class Filters:  # pylint: disable=too-few-public-methods
        """Toggle on or off various filters."""

        class Contrast:  # pylint: disable=too-few-public-methods
            """Discard points with low contrast values."""

            def __init__(
                self, enabled=None, threshold=None,
            ):
                """Initialize contrast filter.

                Args:
                    enabled: a bool
                    threshold: a real number

                """
                self.enabled = enabled
                self.threshold = threshold

            def __eq__(self, other):
                if self.enabled == other.enabled and self.threshold == other.threshold:
                    return True
                return False

            def __str__(self):
                return """Contrast:
enabled: {}
threshold: {}""".format(
                    self.enabled, self.threshold
                )

        class Outlier:  # pylint: disable=too-few-public-methods
            """Outlier filter based on connected components."""

            def __init__(
                self, enabled=None, threshold=None,
            ):
                """Initialize outlier filter.

                Args:
                    enabled: a bool
                    threshold: a real number

                """
                self.enabled = enabled
                self.threshold = threshold

            def __eq__(self, other):
                if self.enabled == other.enabled and self.threshold == other.threshold:
                    return True
                return False

            def __str__(self):
                return """Outlier:
enabled: {}
threshold: {}""".format(
                    self.enabled, self.threshold
                )

        #         class Saturated:  # pylint: disable=too-few-public-methods
        #             """Discard pixels that are saturated in the image."""
        #
        #             def __init__(
        #                 self, enabled=_zivid.Settings().filters.saturated.enabled.value
        #             ):
        #                 """Initialize saturated filter.
        #
        #                 Args:
        #                     enabled: a bool
        #
        #                 """
        #                 self.enabled = enabled
        #
        #             def __eq__(self, other):
        #                 if self.enabled == other.enabled:
        #                     return True
        #                 return False
        #
        #             def __str__(self):
        #                 return """Saturated:
        # enabled: {}""".format(
        #                     self.enabled
        #                 )
        class Reflection:  # pylint: disable=too-few-public-methods
            """Represents camera reflection filter."""

            def __init__(
                self, enabled=None,
            ):
                """Initialize reflection filter.

                Args:
                    enabled: a bool

                """
                self.enabled = enabled

            def __eq__(self, other):
                if self.enabled == other.enabled:
                    return True
                return False

            def __str__(self):
                return """Reflection:
enabled: {}""".format(
                    self.enabled
                )

        #         class Gaussian:  # pylint: disable=too-few-public-methods
        #             """Gaussian smoothing of the point cloud."""
        #
        #             def __init__(
        #                 self,
        #                 enabled=_zivid.Settings().filters.gaussian.enabled.value,
        #                 sigma=_zivid.Settings().filters.gaussian.sigma.value,
        #             ):
        #                 """Initialize gaussian filter.
        #
        #                 Args:
        #                     enabled: a bool
        #                     sigma: a real number
        #
        #                 """
        #                 self.enabled = enabled
        #                 self.sigma = sigma
        #
        #             def __eq__(self, other):
        #                 if self.enabled == other.enabled and self.sigma == other.sigma:
        #                     return True
        #                 return False
        #
        #             def __str__(self):
        #                 return """Gaussian:
        # enabled: {}
        # sigma: {}""".format(
        #                     self.enabled, self.sigma
        #                 )
        def __init__(  # pylint: disable=too-many-arguments
            self,
            contrast=Contrast(),
            outlier=Outlier(),
            # saturated=Saturated(),
            reflection=Reflection(),
            # gaussian=Gaussian(),
        ):
            """Initialize filters.

            Args:
                contrast: a contrast filter object
                outlier: a outlier filter object
                saturated: a saturated filter object
                reflection: a reflection filter object
                gaussian: a gaussian filter object

            """
            self.contrast = contrast
            self.outlier = outlier
            # self.saturated = saturated
            self.reflection = reflection
            # self.gaussian = gaussian

        def __eq__(self, other):
            if (
                self.contrast == other.contrast
                and self.outlier == other.outlier
                # and self.saturated == other.saturated
                and self.reflection == other.reflection
                # and self.gaussian == other.gaussian
            ):
                return True
            return False

        def __str__(self):
            return """Filters:
contrast: {}
outlier: {}
reflection: {}""".format(
                self.contrast, self.outlier, self.reflection,
            )

    def __init__(
        self,
        bidirectional=None,
        brightness=None,
        exposure_time=None,
        filters=Filters(),
        gain=None,
        iris=None,
        red_balance=_zivid.Settings().redbalance.value,
    ):
        # self.bidirectional=
        pass
