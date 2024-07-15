from playwright.async_api import Page
from functools import lru_cache
from Metodos import getFromAPI

@lru_cache
async def Auto_Sub(page: Page, index: int):
    
    id_interno = await getFromAPI.API_Req(page=page, index=index)
    baseURL = 'https://sereduc.blackboard.com/'
    # rootURL = f'{baseURL}webapps/blackboard/execute/recycler?course_id={id_interno}&action=select&context=COURSE#'
    inscryption = f'{baseURL}webapps/blackboard/execute/editCourseEnrollment?course_id={id_interno}&sourceType=COURSES'
    API_User = f'{baseURL}learn/api/public/v1/users/me'
    
    await page.goto(API_User, wait_until='commit')
    user = await page.evaluate('JSON.parse(document.body.innerText).userName')
    
    await page.goto(url=inscryption, wait_until='commit')
    
    await page.locator('#userName').fill(user)
    await page.locator('#courseRoleId').select_option('adsala')
    await page.locator('#bottom_Submit').click()
    await page.wait_for_load_state('load')
    

@lru_cache
async def Auto_Unsub(page: Page, index: int):
    
    id_interno = await getFromAPI.API_Req(page=page, index=index)
    baseURL = 'https://sereduc.blackboard.com/'
    
    # rootURL = f'{baseURL}webapps/blackboard/execute/recycler?course_id='\
    #     f'{id_interno}&action=select&context=COURSE#'
    # offset = 9999
    
    # verify if the user shows up if not verify pagination
    # inscryption = f'{baseURL}webapps/blackboard/execute/courseEnrollment?'\
    #     f'sortCol=userrole&sourceType=COURSES&numResults={offset}&course_id='\
    #     f'{id_interno}&sortDir=DESCENDING'
    
    classUrlUltra = f'{baseURL}ultra/courses/{id_interno}/outline'
    API_User = f'{baseURL}learn/api/public/v1/users/me'
    
    await page.goto(API_User, wait_until='commit')
    user = await page.evaluate('JSON.parse(document.body.innerText).userName')
    
    await page.goto(url=classUrlUltra, wait_until='commit')
    await page.wait_for_load_state('load')
    await page.locator('#course-outline-roster-link').click()
    await page.locator('#search-button').click()
    await page.locator('#search-roster-field').fill(user)
    await page.press('body', 'Enter')
    await page.locator('#rosterView-list > ul > li > div > div.medium-5.columns > div > div').click()
    await page.wait_for_load_state('load')
    await page.locator('#roster-settings > ng-form > div.nested-panel > div > div > div.element-card.account > button').click()
    await page.locator('body > div.panel-has-focus > div > footer > div > div.reveal-modal__footer-buttons > span:nth-child(2) > button').click()
    await page.wait_for_load_state('load')