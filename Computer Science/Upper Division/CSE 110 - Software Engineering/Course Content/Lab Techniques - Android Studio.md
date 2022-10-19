#Java #Practical
## Lab 1: Android, Android Studio, JUnit
- Creating a New Application
	- Configure to minimum Android SDK 28. Select Java instead of Kotlin.
	- Accepting the Android SDK License
- Java code, Resources (XML), Configuration (Manifest and Gradle)
- Basic UI
- In an onCreate(Bundle optional), we can use setContentView(R.layout.activity_name); in order to show the XML on our (Java) activity file.
- Find XML elements by id within the Java file through findViewById(R.id.name);. Then you can mess with it how you wish.
- Debugging and Logging (Logcat and Log.d("<tag\>", "message");)
- Unit Testing
	- JUnit goes in the "test" file, are unit tests, and run on JVM
		- Robolectric(?) needs @RunWith(AndroidJUnit4.class)
		- **ActivityScenario(Rule)** (***REVIEW!***)

## Lab 2: Continuous Integration (CI) with GitHub Actions
- UI -> Integration -> Unit
	- UI uses Espresso and Integration uses androidTest directory
- Enabling GitHub Actions: the .yaml file
- "Record Espresso Test"
- Don't run UI tests on CI 

## Lab 3: ZenHub 
- Git Review

## Lab 4: Activities, Persistence, Background Work

## Lab 5: Assets, RecyclerView, Room

## Lab 6: Documentation, Debugging, Java Stream APIs