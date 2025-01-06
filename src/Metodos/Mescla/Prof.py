from playwright.async_api import Page


async def prof_access(page: Page, id_interno: int) -> None:
    
    url = f'./learn/api/public/v1/courses/{id_interno}/users'
    def url_user(i: int, userID='userId'): return f'./learn/api/public/v1/users/{filtered_users[i][userID]}'
    
    await page.goto(url=url, wait_until='commit')
    data = await page.evaluate('JSON.parse(document.body.innerText)')
    
    filtered_users = []
    for user in data["results"]:
        if user.get("availability", {}).get("available") == "No" and user.get("courseRoleId") == "Instructor":
            filtered_users.append(
                {
                    "availability.available": user["availability"]["available"],
                    "courseRoleId": user["courseRoleId"],
                    "userId": user["userId"],
                }
            )
        
    user_name = []
    i = 0
    for user in filtered_users:
        new_url = url_user(i)
        
        await page.goto(new_url, wait_until='commit')
        data = await page.evaluate('JSON.parse(document.body.innerText)')
        
        # user_name.append(f'{data['name']['given']} {data['name']['family']}')
        user_name.append(f'{data['userName']}')
        i+=1
        
    classUrlUltra = f'./ultra/courses/{id_interno}/outline'
    await page.goto(url=classUrlUltra, wait_until='commit')
    await page.wait_for_load_state('load')
    await page.locator('#course-outline-roster-link').click()
    await page.locator('#search-button').click()
    
    for user in user_name:
        await page.locator('#search-roster-field').fill(user)
        await page.wait_for_timeout(1500)
        await page.press('body', 'Enter')
        await page.press('#search-roster-field', 'Enter')
        await page.wait_for_load_state('load')
        await page.wait_for_load_state('domcontentloaded')
        await page.wait_for_load_state('networkidle')
        try:
            await page.locator('#rosterView-list > ul > li > div > div.medium-5.columns > div > div').click(timeout=3*1000)
            await page.wait_for_load_state('load')
            await page.get_by_text("Permitir acesso ao curso").wait_for(state='visible', timeout=2*1000)
            await page.get_by_text("Permitir acesso ao curso").click()
            await page.get_by_role("button", name="Salvar").click()
            await page.wait_for_load_state('load')
            await page.wait_for_load_state('domcontentloaded')
            await page.wait_for_load_state('networkidle')
            await page.wait_for_timeout(1500)
        except Exception as e:
            await page.locator('#rosterView-grid > ul > li > div > a > bb-username > bb-ui-username > div > div').click()
            await page.wait_for_load_state('load')
            await page.get_by_text("Permitir acesso ao curso").wait_for(state='visible', timeout=2*1000)
            await page.get_by_text("Permitir acesso ao curso").click()
            await page.get_by_role("button", name="Salvar").click()
            await page.wait_for_load_state('load')
            await page.wait_for_load_state('domcontentloaded')
            await page.wait_for_load_state('networkidle')
            await page.wait_for_timeout(1500)