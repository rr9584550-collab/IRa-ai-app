with open('./app/src/main/java/com/example/ui/screens/SettingsScreen.kt', 'r') as f:
    content = f.read()

# I want to add a button for Notification Access in SettingsScreen
# First, I'll add an intent launcher if I need to. But let's pass a function from MainActivity instead,
# or simply use LocalContext to open the intent.

notification_access_code = """
            item {
                SettingsCard {
                    val context = androidx.compose.ui.platform.LocalContext.current
                    SettingsCardTitle(icon = Icons.Default.NotificationsActive, title = "WhatsApp/Notification Access", iconColor = Color(0xFF4CAF50))
                    Spacer(modifier = Modifier.height(16.dp))
                    Button(
                        onClick = {
                            val intent = android.content.Intent("android.settings.ACTION_NOTIFICATION_LISTENER_SETTINGS")
                            context.startActivity(intent)
                        },
                        modifier = Modifier.fillMaxWidth().height(50.dp),
                        colors = ButtonDefaults.buttonColors(containerColor = AccentRed),
                        shape = RoundedCornerShape(8.dp)
                    ) {
                        Text("Enable Notification Access", color = Color.White, fontWeight = FontWeight.Bold, fontSize = 16.sp)
                    }
                    Spacer(modifier = Modifier.height(8.dp))
                    Text("Required for reading WhatsApp and SMS from status bar", color = Color.Gray, fontSize = 12.sp)
                }
            }
"""

content = content.replace(
    'item {\n                Spacer(modifier = Modifier.height(32.dp))\n            }',
    notification_access_code + '\n            item {\n                Spacer(modifier = Modifier.height(32.dp))\n            }'
)

with open('./app/src/main/java/com/example/ui/screens/SettingsScreen.kt', 'w') as f:
    f.write(content)
