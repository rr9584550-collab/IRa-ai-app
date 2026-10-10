with open('app/src/main/java/com/example/ui/screens/HomeScreen.kt', 'r') as f:
    content = f.read()

content = content.replace(
    'onSettingsClick: () -> Unit',
    'onSettingsClick: () -> Unit,\n    onLogsClick: () -> Unit'
)

content = content.replace(
    '''IconButton(onClick = { /* TODO */ }) {
                    Icon(Icons.Default.Notifications, contentDescription = "Notifications", tint = Color.White)
                }''',
    '''IconButton(onClick = onLogsClick) {
                    Icon(Icons.Default.List, contentDescription = "Logs", tint = Color.White)
                }'''
)

with open('app/src/main/java/com/example/ui/screens/HomeScreen.kt', 'w') as f:
    f.write(content)
