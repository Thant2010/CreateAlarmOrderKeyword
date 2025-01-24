from PyQt5.QtWidgets import QSpacerItem, QSizePolicy


class LayoutSpacer:

    @staticmethod
    def verticalExpandingSpacer():
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        return spacer

    @staticmethod
    def horizontalExpandingSpacer():
        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        return spacer

    @staticmethod
    def verticalFixedSpacer(height):
        spacer = QSpacerItem(20, height, QSizePolicy.Minimum, QSizePolicy.Fixed)
        return spacer

    @staticmethod
    def horizontalFixedSpacer(width):
        spacer = QSpacerItem(width, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        return spacer

