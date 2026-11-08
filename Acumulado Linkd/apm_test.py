import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QTabWidget, QLabel, QFrame)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class TurbineAnalysisApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Analysis Summary - AOG LM6000 AERO")
        self.setGeometry(100, 100, 1200, 800)

        # Main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)

        # Sidebar (vertical menu)
        sidebar = QFrame()
        sidebar.setFixedWidth(200)
        sidebar.setStyleSheet("background-color: #1F252A; color: #FFFFFF;")
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setAlignment(Qt.AlignTop)

        # GE Logo
        logo_label = QLabel(self)
        pixmap = QPixmap("ge_logo.png")  # Replace with actual GE logo path
        pixmap = pixmap.scaled(150, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo_label.setPixmap(pixmap)
        sidebar_layout.addWidget(logo_label, alignment=Qt.AlignCenter)

        # Menu items
        menu_items = ["Analysis Summary", "Reliability", "Gen Test", "Out Test"]
        for item in menu_items:
            menu_label = QLabel(item)
            menu_label.setStyleSheet("padding: 10px; font-size: 14px;")
            sidebar_layout.addWidget(menu_label)

        # Spacer to push content to top
        sidebar_layout.addStretch()

        # Main content area
        content_frame = QFrame()
        content_frame.setStyleSheet("background-color: #F5F6F5;")
        content_layout = QVBoxLayout(content_frame)

        # Top tab widget for turbine families
        turbine_tabs = QTabWidget()
        turbine_tabs.setStyleSheet("QTabWidget::pane { border: 0; }")
        turbine_families = ["LM6000", "LM2500", "LM5000"]
        for family in turbine_families:
            tab = QWidget()
            tab_layout = QHBoxLayout(tab)

            # Side tab widget within each turbine family tab
            side_tabs = QTabWidget()
            side_tabs.setFixedWidth(200)
            side_tabs.setStyleSheet("background-color: #E0E0E0;")
            side_tab_content = QWidget()
            side_tab_layout = QVBoxLayout(side_tab_content)
            side_tab_layout.addWidget(QLabel("Distribution Type: Weibull\nFit Method: Least Squares\nConfidence Level: 90%"))
            side_tab_layout.addWidget(QLabel("Mean: 2.265 TTF\nStandard Deviation: 0.865444\nR Squared: 0.996"))
            side_tabs.addTab(side_tab_content, "Distribution Options")

            # Main content for plots and summary
            main_content = QWidget()
            main_content_layout = QVBoxLayout(main_content)
            plot_area = QLabel("Placeholder for Probability Distribution Function Plot")
            plot_area.setStyleSheet("background-color: white; border: 1px solid gray; padding: 10px;")
            cdf_area = QLabel("Placeholder for Cumulative Distribution Function Plot")
            cdf_area.setStyleSheet("background-color: white; border: 1px solid gray; padding: 10px;")
            summary = QLabel("Analysis Summary Data")
            summary.setStyleSheet("background-color: #E8ECEF; border: 1px solid gray; padding: 10px;")

            main_content_layout.addWidget(plot_area)
            main_content_layout.addWidget(cdf_area)
            main_content_layout.addWidget(summary)

            tab_layout.addWidget(side_tabs)
            tab_layout.addWidget(main_content)
            turbine_tabs.addTab(tab, family)

        content_layout.addWidget(turbine_tabs)

        # Combine sidebar and content
        main_layout.addWidget(sidebar)
        main_layout.addWidget(content_frame)

        # Set GE branding and style
        self.setStyleSheet("""
            QMainWindow {
                background-color: #F5F6F5;
            }
            QTabBar::tab {
                background: #D3D8DE;
                padding: 10px;
                margin-right: 2px;
            }
            QTabBar::tab:selected {
                background: #A9B7C3;
            }
        """)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TurbineAnalysisApp()
    window.show()
    sys.exit(app.exec_())