with open('app/src/main/java/com/example/MainActivity.kt', 'r') as f:
    content = f.read()

content = content.replace(
    'import com.example.ui.screens.SettingsScreen',
    'import com.example.ui.screens.SettingsScreen\nimport com.example.ui.screens.LogsScreen'
)

main_content = """                                    com.example.ui.screens.HomeScreen(
                                        iraState = iraState,
                                        onSettingsClick = { currentScreen = Screen.Settings },
                                        onLogsClick = { currentScreen = Screen.Logs }
                                    )"""
content = content.replace(
    '''                                    com.example.ui.screens.HomeScreen(
                                        iraState = iraState,
                                        onSettingsClick = { currentScreen = Screen.Settings }
                                    )''', main_content
)

settings_content = """                    Screen.Settings -> {
                        SettingsScreen(
                            onNavigateBack = { currentScreen = Screen.Home }
                        )
                    }
                    Screen.Logs -> {
                        LogsScreen(
                            onNavigateBack = { currentScreen = Screen.Home }
                        )
                    }"""
content = content.replace(
    '''                    Screen.Settings -> {
                        SettingsScreen(
                            onNavigateBack = { currentScreen = Screen.Home }
                        )
                    }''', settings_content
)

with open('app/src/main/java/com/example/MainActivity.kt', 'w') as f:
    f.write(content)
