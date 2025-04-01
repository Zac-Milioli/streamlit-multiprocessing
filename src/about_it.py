about_it_text = """
## :red[The Problem] with Multiprocessing in Streamlit
If you're using Streamlit (>=1.44.0) alongside more complex processing, you might have encountered an issue: it cannot render UI elements during thread/process events and it does not share session variables across these threads/processes, even if they remain static throughout execution.

This limitation can be a major hurdle for those looking to build more scalable web applications—whether for scientific purposes or simply to develop a robust MVP for their company.

## :orange[The story behind it]
After working with Streamlit for nearly two years, I found myself pushing for more optimized applications for the MVPs and solutions I was developing for some teams from the group I work for. However, the best optimization approach—multiprocessing—turned out to be the barrier.

When I first implemented threads for handling API calls and post-processing tasks, I noticed that none of the toast notifications or progress bars were rendering. Additionally, the console was flooded with "MissingMainThread" logs. Through experimentation, I discovered that while the threads were indeed executing as expected, no UI elements were rendered and some functions failed due to the inability to use the session_state variable during thread events.

The solution began to take shape once I removed all Streamlit components and any usage of session_state from the functions executed by the threads, the excessive logs disappeared. Moreover, everything returned to normal once the threads completed their life cycle.

The remaining challenge was determining when it would be safe to reintroduce Streamlit components. I needed to be able to display progress to the user during thread execution. The answer was straightforward: use them only during thread/process creation or when gathering the results.

## :green[The Solution]
For multiprocessing to work effectively with Streamlit, keep one critical point in mind:

### Streamlit does not handle developer-implemented multiprocessing well, so avoid integrating it directly.
This guideline translates into the following rules:

- Do not use Streamlit components within multiprocessing functions.
- Do not import or use functions that themselves import Streamlit in a multiprocessing context.

Additionally, note that:

### The most appropriate moments to incorporate Streamlit are during thread/process creation or when collecting their results.
If you follow these recommendations, your multiprocessing implementation will work seamlessly with Streamlit.

For session_state variables that remain unchanged during execution, simply convert them into standard Python variables and pass them as function arguments within threads/processes. Progress bars, notifications, and other components should only be rendered outside the multiprocessing context.
"""