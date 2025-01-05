import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QWidget, QTabWidget, QTextEdit, QFileDialog, 
    QCheckBox, QMessageBox, QGroupBox, QComboBox, QScrollArea, QGridLayout
)
from PyQt5.QtCore import QThread, pyqtSignal
import subprocess

class CommandRunner(QThread):
    output_signal = pyqtSignal(str)
    error_signal = pyqtSignal(str)

    def __init__(self, command):
        super().__init__()
        self.command = command

    def run(self):
        try:
            process = subprocess.Popen(
                self.command, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE, 
                shell=True
            )
            stdout, stderr = process.communicate()
            if process.returncode == 0:
                self.output_signal.emit(stdout.decode('utf-8'))
            else:
                self.error_signal.emit(stderr.decode('utf-8'))
        except Exception as e:
            self.error_signal.emit(str(e))

class DIGToolGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Professional DIG Tool GUI")
        self.setGeometry(100, 100, 1000, 800)
        
        # Main layout
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        
        # Command preview
        preview_group = QGroupBox("Command Preview")
        preview_layout = QVBoxLayout()
        self.command_preview = QLineEdit()
        self.command_preview.setReadOnly(True)
        self.command_preview.setPlaceholderText("Command preview will appear here")
        preview_layout.addWidget(self.command_preview)
        preview_group.setLayout(preview_layout)
        
        # Tabs
        self.tabs = QTabWidget()
        self.setup_basic_tab()
        self.setup_query_options_tab()
        self.setup_display_options_tab()
        self.setup_advanced_tab()
        self.setup_logs_tab()
        
        # Result output
        result_group = QGroupBox("Query Result")
        result_layout = QVBoxLayout()
        self.result_output = QTextEdit()
        self.result_output.setReadOnly(True)
        result_layout.addWidget(self.result_output)
        result_group.setLayout(result_layout)
        
        # Execute button
        self.execute_button = QPushButton("Execute Query")
        self.execute_button.clicked.connect(self.execute_command)
        self.execute_button.setStyleSheet("background-color: #4CAF50; color: white; padding: 8px;")
        
        # Add all components to main layout
        main_layout.addWidget(preview_group)
        main_layout.addWidget(self.tabs)
        main_layout.addWidget(self.execute_button)
        main_layout.addWidget(result_group)
        
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def setup_basic_tab(self):
        basic_tab = QWidget()
        layout = QVBoxLayout()
        
        # Basic query inputs
        query_group = QGroupBox("Basic Query Settings")
        query_layout = QGridLayout()
        
        self.domain_input = QLineEdit()
        self.domain_input.setPlaceholderText("Enter domain (e.g., example.com)")
        
        self.query_type_combo = QComboBox()
        query_types = ["A", "AAAA", "MX", "NS", "SOA", "TXT", "CNAME", "PTR", "SRV", "ANY"]
        self.query_type_combo.addItems(query_types)
        
        self.query_class_combo = QComboBox()
        query_classes = ["IN", "CH", "HS"]
        self.query_class_combo.addItems(query_classes)
        
        query_layout.addWidget(QLabel("Domain:"), 0, 0)
        query_layout.addWidget(self.domain_input, 0, 1)
        query_layout.addWidget(QLabel("Query Type:"), 1, 0)
        query_layout.addWidget(self.query_type_combo, 1, 1)
        query_layout.addWidget(QLabel("Query Class:"), 2, 0)
        query_layout.addWidget(self.query_class_combo, 2, 1)
        
        query_group.setLayout(query_layout)
        layout.addWidget(query_group)
        
        basic_tab.setLayout(layout)
        self.tabs.addTab(basic_tab, "Basic Settings")

    def setup_query_options_tab(self):
        query_tab = QScrollArea()
        query_tab.setWidgetResizable(True)
        query_widget = QWidget()
        layout = QVBoxLayout()

        # Transport options
        transport_group = QGroupBox("Transport Options")
        transport_layout = QVBoxLayout()
        
        self.tcp_checkbox = QCheckBox("Use TCP (+tcp)")
        self.ipv4_checkbox = QCheckBox("Use IPv4 only (-4)")
        self.ipv6_checkbox = QCheckBox("Use IPv6 only (-6)")
        
        transport_layout.addWidget(self.tcp_checkbox)
        transport_layout.addWidget(self.ipv4_checkbox)
        transport_layout.addWidget(self.ipv6_checkbox)
        transport_group.setLayout(transport_layout)
        
        # Query flags
        flags_group = QGroupBox("Query Flags")
        flags_layout = QVBoxLayout()
        
        self.dnssec_checkbox = QCheckBox("Request DNSSEC records (+dnssec)")
        self.cd_flag_checkbox = QCheckBox("Set CD flag (+cdflag)")
        self.ra_flag_checkbox = QCheckBox("Set RA flag (+raflag)")
        self.aa_flag_checkbox = QCheckBox("Set AA flag (+aaflag)")
        
        flags_layout.addWidget(self.dnssec_checkbox)
        flags_layout.addWidget(self.cd_flag_checkbox)
        flags_layout.addWidget(self.ra_flag_checkbox)
        flags_layout.addWidget(self.aa_flag_checkbox)
        flags_group.setLayout(flags_layout)
        
        layout.addWidget(transport_group)
        layout.addWidget(flags_group)
        
        query_widget.setLayout(layout)
        query_tab.setWidget(query_widget)
        self.tabs.addTab(query_tab, "Query Options")

    def setup_display_options_tab(self):
        display_tab = QScrollArea()
        display_tab.setWidgetResizable(True)
        display_widget = QWidget()
        layout = QVBoxLayout()
        
        # Display controls
        display_group = QGroupBox("Display Options")
        display_layout = QVBoxLayout()
        
        self.short_checkbox = QCheckBox("Short output (+short)")
        self.multiline_checkbox = QCheckBox("Multiline output (+multiline)")
        self.stats_checkbox = QCheckBox("Show statistics (+stats)")
        self.comments_checkbox = QCheckBox("Show comments (+comments)")
        self.ttl_units_checkbox = QCheckBox("Show TTL in human-readable units (+ttlunits)")
        
        display_layout.addWidget(self.short_checkbox)
        display_layout.addWidget(self.multiline_checkbox)
        display_layout.addWidget(self.stats_checkbox)
        display_layout.addWidget(self.comments_checkbox)
        display_layout.addWidget(self.ttl_units_checkbox)
        display_group.setLayout(display_layout)
        
        layout.addWidget(display_group)
        display_widget.setLayout(layout)
        display_tab.setWidget(display_widget)
        self.tabs.addTab(display_tab, "Display Options")

    def setup_advanced_tab(self):
        advanced_tab = QScrollArea()
        advanced_tab.setWidgetResizable(True)
        advanced_widget = QWidget()
        layout = QVBoxLayout()
        
        # Timing options
        timing_group = QGroupBox("Timing Options")
        timing_layout = QGridLayout()
        
        self.timeout_input = QLineEdit()
        self.timeout_input.setPlaceholderText("Query timeout in seconds")
        self.retry_input = QLineEdit()
        self.retry_input.setPlaceholderText("Number of retries")
        
        timing_layout.addWidget(QLabel("Timeout:"), 0, 0)
        timing_layout.addWidget(self.timeout_input, 0, 1)
        timing_layout.addWidget(QLabel("Retries:"), 1, 0)
        timing_layout.addWidget(self.retry_input, 1, 1)
        timing_group.setLayout(timing_layout)
        
        # Additional options
        options_group = QGroupBox("Additional Options")
        options_layout = QVBoxLayout()
        
        self.additional_options_input = QLineEdit()
        self.additional_options_input.setPlaceholderText("Additional DIG options")
        options_layout.addWidget(self.additional_options_input)
        options_group.setLayout(options_layout)
        
        layout.addWidget(timing_group)
        layout.addWidget(options_group)
        
        advanced_widget.setLayout(layout)
        advanced_tab.setWidget(advanced_widget)
        self.tabs.addTab(advanced_tab, "Advanced Options")

    def setup_logs_tab(self):
        logs_tab = QWidget()
        layout = QVBoxLayout()
        
        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)
        
        save_log_button = QPushButton("Save Logs")
        save_log_button.clicked.connect(self.save_logs)
        clear_log_button = QPushButton("Clear Logs")
        clear_log_button.clicked.connect(self.clear_logs)
        
        button_layout = QHBoxLayout()
        button_layout.addWidget(save_log_button)
        button_layout.addWidget(clear_log_button)
        
        layout.addWidget(QLabel("Operation Logs:"))
        layout.addWidget(self.log_output)
        layout.addLayout(button_layout)
        
        logs_tab.setLayout(layout)
        self.tabs.addTab(logs_tab, "Logs")

    def execute_command(self):
        # Build command string from all options
        command_parts = ["dig"]
        
        # Basic options
        domain = self.domain_input.text()
        if not domain:
            QMessageBox.warning(self, "Warning", "Please enter a domain name.")
            return
        
        command_parts.append(domain)
        command_parts.append(f"-t {self.query_type_combo.currentText()}")
        command_parts.append(f"-c {self.query_class_combo.currentText()}")
        
        # Transport options
        if self.tcp_checkbox.isChecked():
            command_parts.append("+tcp")
        if self.ipv4_checkbox.isChecked():
            command_parts.append("-4")
        if self.ipv6_checkbox.isChecked():
            command_parts.append("-6")
        
        # Query flags
        if self.dnssec_checkbox.isChecked():
            command_parts.append("+dnssec")
        if self.cd_flag_checkbox.isChecked():
            command_parts.append("+cdflag")
        if self.ra_flag_checkbox.isChecked():
            command_parts.append("+raflag")
        if self.aa_flag_checkbox.isChecked():
            command_parts.append("+aaflag")
        
        # Display options
        if self.short_checkbox.isChecked():
            command_parts.append("+short")
        if self.multiline_checkbox.isChecked():
            command_parts.append("+multiline")
        if self.stats_checkbox.isChecked():
            command_parts.append("+stats")
        if self.comments_checkbox.isChecked():
            command_parts.append("+comments")
        if self.ttl_units_checkbox.isChecked():
            command_parts.append("+ttlunits")
        
        # Timing options
        if self.timeout_input.text():
            command_parts.append(f"+timeout={self.timeout_input.text()}")
        if self.retry_input.text():
            command_parts.append(f"+retry={self.retry_input.text()}")
        
        # Additional options
        if self.additional_options_input.text():
            command_parts.append(self.additional_options_input.text())
        
        # Build and execute command
        command = " ".join(command_parts)
        self.command_preview.setText(command)
        self.log_output.append(f"Executing command: {command}\n")
        
        self.thread = CommandRunner(command)
        self.thread.output_signal.connect(self.display_result)
        self.thread.error_signal.connect(self.display_error)
        self.thread.start()

    def display_result(self, result):
        self.result_output.setText(result)
        self.log_output.append(f"SUCCESS:\n{result}\n")

    def display_error(self, error):
        QMessageBox.critical(self, "Error", error)
        self.log_output.append(f"ERROR:\n{error}\n")

    def save_logs(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Logs",
            "",
            "Text Files (*.txt);;All Files (*)",
            options=options
        )
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(self.log_output.toPlainText())
                QMessageBox.information(self, "Success", "Logs saved successfully.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save logs: {str(e)}")

    def clear_logs(self):
        self.log_output.clear()
        QMessageBox.information(self, "Success", "Logs cleared successfully.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DIGToolGUI()
    window.show()
    sys.exit(app.exec_())