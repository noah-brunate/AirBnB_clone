 <h1 class="gap">0x00. AirBnB clone - The console</h1>
<h2> This a team project of Noah And Bruno </h2>

<em>For this project, we expect you to look at these concepts:</em> </p>

<ul>
<li><a href="/concepts/66">Python packages</a> </li>
<li> <a href="/concepts/74">AirBnB clone</a> </li>
</ul>

<h2>Background Context</h2>

<h3>Welcome to the AirBnB clone project!</h3>

<p>Before starting, please read the <strong>AirBnB</strong> concept page.</p>

<h4>First step: Write a command interpreter to manage your AirBnB objects.</h4>

<p>This is the first step towards building your first full web application: the <strong>AirBnB clone</strong>.
This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration&hellip; </p>

<p>Each task is linked and will help you to:</p>

<ul>
<li>put in place a parent class (called <code>BaseModel</code>) to take care of the initialization, serialization and deserialization of your future instances</li>
<li>create a simple flow of serialization/deserialization: Instance &lt;-&gt; Dictionary &lt;-&gt; JSON string &lt;-&gt; file</li>
<li>create all classes used for AirBnB (<code>User</code>, <code>State</code>, <code>City</code>, <code>Place</code>&hellip;) that inherit from <code>BaseModel</code></li>
<li>create the first abstracted storage engine of the project: File storage. </li>
<li>create all unittests to validate all our classes and storage engine</li>
</ul>

<h3>What&rsquo;s a command interpreter?</h3>

<p>Do you remember the Shell? It&rsquo;s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:</p>

<ul>
<li>Create a new object (ex: a new User or a new Place)</li>
<li>Retrieve an object from a file, a database etc&hellip;</li>
<li>Do operations on objects (count, compute stats, etc&hellip;)</li>
<li>Update attributes of an object</li>
<li>Destroy an object</li>
</ul>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/8ecCwE6veBmm3Nppw4hz5A" title="cmd module" target="_blank">cmd module</a> </li>
<li><a href="/rltoken/uEy4RftSdKypoig9NFTvCg" title="cmd module in depth" target="_blank">cmd module in depth</a></li>
<li><strong>packages</strong> concept page</li>
<li><a href="/rltoken/KfL9TqwdI69W6ttG6gTPPQ" title="uuid module" target="_blank">uuid module</a> </li>
<li><a href="/rltoken/1d8I3jSKgnYAtA1IZfEDpA" title="datetime" target="_blank">datetime</a> </li>
<li><a href="/rltoken/IlFiMB8UmqBG2CxA0AD3jA" title="unittest module" target="_blank">unittest module</a> </li>
<li><a href="/rltoken/C_a0EKbtvKdMcwIAuSIZng" title="args/kwargs" target="_blank">args/kwargs</a> </li>
<li><a href="/rltoken/tgNVrKKzlWgS4dfl3mQklw" title="Python test cheatsheet" target="_blank">Python test cheatsheet</a> </li>
<li><a href="/rltoken/EvcaH9uTLlauxuw03WnkOQ" title="cmd module wiki page" target="_blank">cmd module wiki page</a></li>
<li><a href="/rltoken/begh14KQA-3ov29KvD_HvA" title="python unittest" target="_blank">python unittest</a></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/uV5eZkRZ_XEqYbgPd-0CWw" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>How to create a Python package</li>
<li>How to create a command interpreter in Python using the <code>cmd</code> module</li>
<li>What is Unit testing and how to implement it in a large project</li>
<li>How to serialize and deserialize a Class</li>
<li>How to write and read a JSON file</li>
<li>How to manage <code>datetime</code></li>
<li>What is an <code>UUID</code></li>
<li>What is <code>*args</code> and how to use it</li>
<li>What is <code>**kwargs</code> and how to use it</li>
<li>How to handle named arguments in a function</li>
</ul>

<h3>Copyright - Plagiarism</h3>

<ul>
<li>You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.</li>
<li>You will not be able to meet the objectives of this or any following project by copying and pasting someone else&rsquo;s work. </li>
<li>You are not allowed to publish any content of this project.</li>
<li>Any form of plagiarism is strictly forbidden and will result in removal from the program.</li>
</ul>

<h2>Requirements</h2>

<h3>Python Scripts</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the pycodestyle (version <code>2.8.*</code>)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>All your classes should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&#39;</code>)</li>
<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code> and <code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&#39;</code>)</li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
</ul>

<h3>Python Unit Tests</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files should end with a new line</li>
<li>All your test files should be inside a folder <code>tests</code></li>
<li>You have to use the <a href="/rltoken/op1-rQGlw0wwwqNBsn1yaw" title="unittest module" target="_blank">unittest module</a> </li>
<li>All your test files should be python files (extension: <code>.py</code>)</li>
<li>All your test files and folders should start by <code>test_</code></li>
<li>Your file organization in the tests folder should be the same as your project</li>
<li>e.g., For <code>models/base_model.py</code>, unit tests must be in: <code>tests/test_models/test_base_model.py</code></li>
<li>e.g., For <code>models/user.py</code>, unit tests must be in: <code>tests/test_models/test_user.py</code></li>
<li>All your tests should be executed by using this command: <code>python3 -m unittest discover tests</code></li>
<li>You can also test file by file by using this command: <code>python3 -m unittest tests/test_models/test_base_model.py</code></li>
<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>All your classes should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&#39;</code>)</li>
<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code> and <code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&#39;</code>)</li>
<li>We strongly encourage you to work together on test cases, so that you don&rsquo;t miss any edge case</li>
</ul>

 <h2 class="gap">Tasks</h2>
 <h3 class="panel-title"> 0. README, AUTHORS </h3>

<li>Write a <code>README.md</code>:

<ul>
<li>description of the project</li>
<li>description of the command interpreter:

<ul>
<li>how to start it</li>
<li>how to use it</li>
<li>examples</li>
</ul></li>
</ul></li>
<li>You should have an <code>AUTHORS</code> file at the root of your repository, listing all individuals having contributed content to the repository. For format, reference <a href="/rltoken/_8n_z3pf5HWi1l7uv1E9iA" title="Docker&#39;s AUTHORS page" target="_blank">Docker&rsquo;s AUTHORS page</a></li>
<li>You should use branches and pull requests on GitHub - it will help you as team to organize your work</li>
</ul>
<h3 class="panel-title">  1. Be pycodestyle compliant!</h3>
<p>Write beautiful code that passes the pycodestyle checks.</p>

<h3 class="panel-title">  2. Unittests </h3>

 <p>All your files, classes, functions must be tested with unit tests</p>
<h3 class="panel-title">  3. BaseModel  </h3>
 <p>Write a class <code>BaseModel</code> that defines all common attributes/methods for other classes:</p>
<ul>
<li><code>models/base_model.py</code></li>
<li>Public instance attributes: 

<ul>
<li><code>id</code>: string - assign with an <code>uuid</code> when an instance is created:

<ul>
<li>you can use <code>uuid.uuid4()</code> to generate unique <code>id</code> but don&rsquo;t forget to convert to a string</li>
<li>the goal is to have unique <code>id</code> for each <code>BaseModel</code></li>
</ul></li>
<li><code>created_at</code>: datetime - assign with the current datetime when an instance is created</li>
<li><code>updated_at</code>: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object</li>
</ul></li>
<li><code>__str__</code>: should print: <code>[&lt;class name&gt;] (&lt;self.id&gt;) &lt;self.__dict__&gt;</code></li>
<li>Public instance methods:

<ul>
<li><code>save(self)</code>: updates the public instance attribute <code>updated_at</code> with the current datetime</li>
<li><code>to_dict(self)</code>: returns a dictionary containing all keys/values of <code>__dict__</code> of the instance:

<ul>
<li>by using <code>self.__dict__</code>, only instance attributes set will be returned</li>
<li>a key <code>__class__</code> must be added to this dictionary with the class name of the object</li>
<li><code>created_at</code> and <code>updated_at</code> must be converted to string object in ISO format:

<ul>
<li>format: <code>%Y-%m-%dT%H:%M:%S.%f</code> (ex: <code>2017-06-14T22:31:03.285259</code>) </li>
<li>you can use <code>isoformat()</code> of <code>datetime</code> object</li>
</ul></li>
<li>This method will be the first piece of the serialization/deserialization process: create a dictionary representation with &ldquo;simple object type&rdquo; of our <code>BaseModel</code></li>
</ul></li>
</ul></li>
</ul>
 <h3 class="panel-title">  4. Create BaseModel from dictionary  </h3>
<p>Previously we created a method to generate a dictionary representation of an instance (method <code>to_dict()</code>).</p>

<p>Now it&rsquo;s time to re-create an instance with this dictionary representation.</p>

<pre><code>&lt;class &#39;BaseModel&#39;&gt; -&gt; to_dict() -&gt; &lt;class &#39;dict&#39;&gt; -&gt; &lt;class &#39;BaseModel&#39;&gt;
</code></pre>

<p>Update <code>models/base_model.py</code>:</p>

<ul>
<li><code>__init__(self, *args, **kwargs)</code>: 

<ul>
<li>you will use <code>*args, **kwargs</code> arguments for the constructor of a <code>BaseModel</code>. (more information inside the <strong>AirBnB clone</strong> concept page)</li>
<li><code>*args</code> won&rsquo;t be used</li>
<li>if <code>kwargs</code> is not empty:

<ul>
<li>each key of this dictionary is an attribute name (<strong>Note</strong> <code>__class__</code> from <code>kwargs</code> is the only one that should not be added as an attribute. See the example output, below)</li>
<li>each value of this dictionary is the value of this attribute name</li>
<li><strong>Warning</strong>: <code>created_at</code> and <code>updated_at</code> are strings in this dictionary, but inside your <code>BaseModel</code> instance is working with <code>datetime</code> object. You have to convert these strings into <code>datetime</code> object. Tip: you know the string format of these datetime</li>
</ul></li>
<li>otherwise:

<ul>
<li>create <code>id</code> and <code>created_at</code> as you did previously (new instance)</li>
</ul></li>
</ul></li>
</ul>
 <h3 class="panel-title">  5. Store first object </h3>
 <p>Now we can recreate a <code>BaseModel</code> from another one by using a dictionary representation:</p>

<pre><code>&lt;class &#39;BaseModel&#39;&gt; -&gt; to_dict() -&gt; &lt;class &#39;dict&#39;&gt; -&gt; &lt;class &#39;BaseModel&#39;&gt;
</code></pre>

<p>It&rsquo;s great but it&rsquo;s still not persistent: every time you launch the program, you don&rsquo;t restore all objects created before&hellip; The first way you will see here is to save these objects to a file.</p>

<p>Writing the dictionary representation to a file won&rsquo;t be relevant:</p>

<ul>
<li>Python doesn&rsquo;t know how to convert a string to a dictionary (easily)</li>
<li>It&rsquo;s not human readable</li>
<li>Using this file with another program in Python or other language will be hard.</li>
</ul>

<p>So, you will convert the dictionary representation to a JSON string. JSON is a standard representation of a data structure. With this format, humans can read and all programming languages have a JSON reader and writer.</p>

<p>Now the flow of serialization-deserialization will be:</p>
<pre><code>&lt;class &#39;BaseModel&#39;&gt; -&gt; to_dict() -&gt; &lt;class &#39;dict&#39;&gt; -&gt; JSON dump -&gt; &lt;class &#39;str&#39;&gt; -&gt; FILE -&gt; &lt;class &#39;str&#39;&gt; -&gt; JSON load -&gt; &lt;class &#39;dict&#39;&gt; -&gt; &lt;class &#39;BaseModel&#39;&gt;
</code></pre>

<p>Magic right?</p>

<p>Terms:</p>

<ul>
<li><strong>simple Python data structure</strong>: Dictionaries, arrays, number and string. ex: <code>{ &#39;12&#39;: { &#39;numbers&#39;: [1, 2, 3], &#39;name&#39;: &quot;John&quot; } }</code></li>
<li><strong>JSON string representation</strong>: String representing a simple data structure in JSON format. ex: <code>&#39;{ &quot;12&quot;: { &quot;numbers&quot;: [1, 2, 3], &quot;name&quot;: &quot;John&quot; } }&#39;</code></li>
</ul>

<p>Write a class <code>FileStorage</code> that serializes instances to a JSON file and deserializes JSON file to instances:</p>

<ul>
<li><code>models/engine/file_storage.py</code></li>
<li>Private class attributes:

<ul>
<li><code>__file_path</code>: string - path to the JSON file (ex: <code>file.json</code>)</li>
<li><code>__objects</code>: dictionary - empty but will store all objects by <code>&lt;class name&gt;.id</code> (ex: to store a <code>BaseModel</code> object with <code>id=12121212</code>, the key will be <code>BaseModel.12121212</code>)</li>
</ul></li>
<li>Public instance methods:

<ul>
<li><code>all(self)</code>: returns the dictionary <code>__objects</code></li>
<li><code>new(self, obj)</code>: sets in <code>__objects</code> the <code>obj</code> with key <code>&lt;obj class name&gt;.id</code></li>
<li><code>save(self)</code>: serializes <code>__objects</code> to the JSON file (path: <code>__file_path</code>)</li>
<li><code>reload(self)</code>: deserializes the JSON file to <code>__objects</code> (only if the JSON file (<code>__file_path</code>) exists ; otherwise, do nothing. If the file doesn&rsquo;t exist, no exception should be raised)</li>
</ul></li>
</ul>

<p>Update <code>models/__init__.py</code>: to create a unique <code>FileStorage</code> instance for your application</p>

<ul>
<li>import <code>file_storage.py</code></li>
<li>create the variable <code>storage</code>, an instance of <code>FileStorage</code></li>
<li>call <code>reload()</code> method on this variable</li>
</ul>

<p>Update <code>models/base_model.py</code>: to link your <code>BaseModel</code> to <code>FileStorage</code> by using the variable <code>storage</code></p>

<ul>
<li>import the variable <code>storage</code></li>
<li>in the method <code>save(self)</code>:

<ul>
<li>call <code>save(self)</code> method of <code>storage</code></li>
</ul></li>
<li><code>__init__(self, *args, **kwargs)</code>: 

<ul>
<li>if it&rsquo;s a new instance (not from a dictionary representation), add a call to the method <code>new(self)</code> on <code>storage</code></li>
</ul></li>
</ul>
 <h3 class="panel-title">  6. Console 0.0.1  </h3>
<ul>
<li>You must use the module <code>cmd</code></li>
<li>Your class definition must be: <code>class HBNBCommand(cmd.Cmd):</code></li>
<li>Your command interpreter should implement:

<ul>
<li><code>quit</code> and <code>EOF</code> to exit the program</li>
<li><code>help</code> (this action is provided by default by <code>cmd</code> but you should keep it updated and documented as you work through tasks)</li>
<li>a custom prompt: <code>(hbnb)</code></li>
<li>an empty line + <code>ENTER</code> shouldn&rsquo;t execute anything</li>
</ul></li>
<li>Your code should not be executed when imported</li>
</ul>

<p><strong>Warning:</strong></p>

<p>You should end your file with:</p>

<pre><code>if __name__ == &#39;__main__&#39;:
    HBNBCommand().cmdloop()
</code></pre>

<p>to make your program executable except when imported.
Please don&rsquo;t add anything around - the Checker won&rsquo;t like it otherwise</p>
<h3 class="panel-title">  7. Console 0.1 </h3>
 <p>Update your command interpreter (<code>console.py</code>) to have these commands:</p>

<ul>
<li><code>create</code>: Creates a new instance of <code>BaseModel</code>, saves it (to the JSON file) and prints the <code>id</code>. Ex: <code>$ create BaseModel</code> 

<ul>
<li>If the class name is missing, print <code>** class name missing **</code> (ex: <code>$ create</code>)</li>
<li>If the class name doesn&rsquo;t exist, print <code>** class doesn&#39;t exist **</code> (ex: <code>$ create MyModel</code>)</li>
</ul></li>
<li><code>show</code>: Prints the string representation of an instance based on the class name and <code>id</code>. Ex: <code>$ show BaseModel 1234-1234-1234</code>.

<ul>
<li>If the class name is missing, print <code>** class name missing **</code> (ex: <code>$ show</code>)</li>
<li>If the class name doesn&rsquo;t exist, print <code>** class doesn&#39;t exist **</code> (ex: <code>$ show MyModel</code>)</li>
<li>If the <code>id</code> is missing, print <code>** instance id missing **</code> (ex: <code>$ show BaseModel</code>)</li>
<li>If the instance of the class name doesn&rsquo;t exist for the <code>id</code>, print <code>** no instance found **</code> (ex: <code>$ show BaseModel 121212</code>)</li>
</ul></li>
<li><code>destroy</code>: Deletes an instance based on the class name and <code>id</code> (save the change into the JSON file). Ex: <code>$ destroy BaseModel 1234-1234-1234</code>.

<ul>
<li>If the class name is missing, print <code>** class name missing **</code> (ex: <code>$ destroy</code>)</li>
<li>If the class name doesn&rsquo;t exist, print <code>** class doesn&#39;t exist ** (ex:</code>$ destroy MyModel<code>)</code></li>
<li>If the <code>id</code> is missing, print <code>** instance id missing **</code> (ex: <code>$ destroy BaseModel</code>)</li>
<li>If the instance of the class name doesn&rsquo;t exist for the <code>id</code>, print <code>** no instance found **</code> (ex: <code>$ destroy BaseModel 121212</code>)</li>
</ul></li>
<li><code>all</code>: Prints all string representation of all instances based or not on the class name. Ex: <code>$ all BaseModel</code> or <code>$ all</code>.

<ul>
<li>The printed result must be a list of strings (like the example below)</li>
<li>If the class name doesn&rsquo;t exist, print <code>** class doesn&#39;t exist **</code> (ex: <code>$ all MyModel</code>)</li>
</ul></li>
<li><code>update</code>: Updates an instance based on the class name and <code>id</code> by adding or updating attribute (save the change into the JSON file). Ex: <code>$ update BaseModel 1234-1234-1234 email &quot;aibnb@mail.com&quot;</code>.

<ul>
<li>Usage: <code>update &lt;class name&gt; &lt;id&gt; &lt;attribute name&gt; &quot;&lt;attribute value&gt;&quot;</code></li>
<li>Only one attribute can be updated at the time</li>
<li>You can assume the attribute name is valid (exists for this model)</li>
<li>The attribute value must be casted to the attribute type </li>
<li>If the class name is missing, print <code>** class name missing **</code> (ex: <code>$ update</code>)</li>
<li>If the class name doesn&rsquo;t exist, print <code>** class doesn&#39;t exist **</code> (ex: <code>$ update MyModel</code>)</li>
<li>If the <code>id</code> is missing, print <code>** instance id missing **</code> (ex: <code>$ update BaseModel</code>)</li>
<li>If the instance of the class name doesn&rsquo;t exist for the <code>id</code>, print <code>** no instance found **</code>  (ex: <code>$ update BaseModel 121212</code>)</li>
<li>If the attribute name is missing, print <code>** attribute name missing **</code> (ex: <code>$ update BaseModel existing-id</code>)</li>
<li>If the value for the attribute name doesn&rsquo;t exist, print <code>** value missing **</code> (ex: <code>$ update BaseModel existing-id first_name</code>)</li>
<li>All other arguments should not be used (Ex: <code>$ update BaseModel 1234-1234-1234 email &quot;aibnb@mail.com&quot; first_name &quot;Betty&quot;</code> = <code>$ update BaseModel 1234-1234-1234 email &quot;aibnb@mail.com&quot;</code>)</li>
<li><code>id</code>, <code>created_at</code> and <code>updated_at</code> cant&rsquo; be updated. You can assume they won&rsquo;t be passed in the <code>update</code> command</li>
<li>Only &ldquo;simple&rdquo; arguments can be updated: string, integer and float. You can assume nobody will try to update list of ids or datetime</li>
</ul></li>
</ul>

<p>Let&rsquo;s add some rules:</p>

<ul>
<li>You can assume arguments are always in the right order</li>
<li>Each arguments are separated by a space</li>
<li>A string argument with a space must be between double quote</li>
<li>The error management starts from the first argument to the last one<br></li>
</ul>
 <h3 class="panel-title">  8. First User  </h3>
 <p>Write a class <code>User</code> that inherits from <code>BaseModel</code>:</p>

<ul>
<li><code>models/user.py</code></li>
<li>Public class attributes:

<ul>
<li><code>email</code>: string - empty string</li>
<li><code>password</code>: string - empty string</li>
<li><code>first_name</code>: string - empty string</li>
<li><code>last_name</code>: string - empty string</li>
</ul></li>
</ul>

<p>Update <code>FileStorage</code> to manage correctly serialization and deserialization of <code>User</code>.</p>

<p>Update your command interpreter (<code>console.py</code>) to allow <code>show</code>, <code>create</code>, <code>destroy</code>, <code>update</code> and <code>all</code> used with <code>User</code>.</p>
<h3 class="panel-title">  9. More classes!  </h3>
 <p>Write all those classes that inherit from <code>BaseModel</code>:</p>

<ul>
<li><code>State</code> (<code>models/state.py</code>):

<ul>
<li>Public class attributes:

<ul>
<li><code>name</code>: string - empty string</li>
</ul></li>
</ul></li>
<li><code>City</code> (<code>models/city.py</code>):

<ul>
<li>Public class attributes:

<ul>
<li><code>state_id</code>: string - empty string: it will be the <code>State.id</code></li>
<li><code>name</code>: string - empty string</li>
</ul></li>
</ul></li>
<li><code>Amenity</code> (<code>models/amenity.py</code>):

<ul>
<li>Public class attributes:

<ul>
<li><code>name</code>: string - empty string</li>
</ul></li>
</ul></li>
<li><code>Place</code> (<code>models/place.py</code>):

<ul>
<li>Public class attributes:

<ul>
<li><code>city_id</code>: string - empty string: it will be the <code>City.id</code></li>
<li><code>user_id</code>: string - empty string: it will be the <code>User.id</code></li>
<li><code>name</code>: string - empty string</li>
<li><code>description</code>: string - empty string</li>
<li><code>number_rooms</code>: integer - 0</li>
<li><code>number_bathrooms</code>: integer - 0</li>
<li><code>max_guest</code>: integer - 0</li>
<li><code>price_by_night</code>: integer - 0</li>
<li><code>latitude</code>: float - 0.0</li>
<li><code>longitude</code>: float - 0.0</li>
<li><code>amenity_ids</code>: list of string - empty list: it will be the list of <code>Amenity.id</code> later</li>
</ul></li>
</ul></li>
<li><code>Review</code> (<code>models/review.py</code>):

<ul>
<li>Public class attributes:

<ul>
<li><code>place_id</code>: string - empty string: it will be the <code>Place.id</code></li>
<li><code>user_id</code>: string - empty string: it will be the <code>User.id</code></li>
<li><code>text</code>: string - empty string</li>
</ul></li>
</ul></li>
</ul>
<h3 class="panel-title">  10. Console 1.0  </h3>
 <p>Update <code>FileStorage</code> to manage correctly serialization and deserialization of all our new classes: <code>Place</code>, <code>State</code>, <code>City</code>, <code>Amenity</code> and <code>Review</code></p>

<p>Update your command interpreter (<code>console.py</code>) to allow those actions: <code>show</code>, <code>create</code>, <code>destroy</code>, <code>update</code> and <code>all</code> with all classes created previously.</p>

<p>Enjoy your first console!</p>

<p><strong>No unittests needed for the console</strong></p>

